# Generated by Django 4.0.6 on 2022-07-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_remove_account_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Account',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
