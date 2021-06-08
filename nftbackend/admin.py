from django.contrib import admin
from .models import (
    NFT,
    Whitelist,
    Claimant,
    Signature,
    Signer
)

admin.site.register(NFT)
admin.site.register(Whitelist)
admin.site.register(Claimant)
admin.site.register(Signature)
admin.site.register(Signer)