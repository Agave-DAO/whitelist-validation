# Generated by Django 3.2.3 on 2021-06-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftbackend', '0002_signature_signer'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='signature',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
