# Generated by Django 3.2.3 on 2021-06-01 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nftbackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftbackend.signer')),
                ('whitelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftbackend.whitelist')),
            ],
        ),
    ]
