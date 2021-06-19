from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


class NFT(models.Model):
    contract_address = models.CharField(max_length=100)
    token_id = models.BigIntegerField()
    whitelist = models.OneToOneField("Whitelist", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"NFT {self.token_id} on contract {self.contract_address}"


class Whitelist(models.Model):
    whitelist_file = models.FileField()

    @property
    def is_valid(self) -> bool:
        signatures = Signature.objects.filter(whitelist__id=self.id)
        signers = [sig.signer for sig in signatures]

        return len(set(signer.address for signer in signers)) > Signer.objects.count() * 3 / 4

    def __str__(self) -> str:
        return f"Whitelist for NFT {self.nft}"


class Signature(models.Model):
    signature = models.CharField(max_length=400)
    signer = models.ForeignKey("Signer", on_delete=models.CASCADE)
    whitelist = models.ForeignKey("Whitelist", on_delete=models.CASCADE)

    def __str__(self):
        return f"Signature from <{self.signer.address}> on {self.whitelist}"

    class Meta:
        unique_together = (
            'signer',
            'whitelist'
        )


class Claimant(models.Model):
    whitelist = models.ForeignKey("Whitelist", on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    has_claimed = models.BooleanField(default=False)

    @property
    def can_claim(self):
        return self.whitelist.signature_set.count() > Signer.objects.count() * 3 / 4

    class Meta:
        unique_together = (
            'whitelist',
            'address'
        )


class Signer(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"Signer <{self.address}>"


@receiver(post_save, sender=Whitelist)
@transaction.atomic
def create_claimants(sender, instance: Whitelist, **kwargs):
    for line in instance.whitelist_file:
        Claimant.objects.create(
            whitelist=instance,
            address=line.decode(),
            has_claimed=False
        )