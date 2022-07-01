# Generated by Django 4.0.5 on 2022-06-30 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('Ms', 'Ms'), ('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Miss', 'Miss')], max_length=50),
        ),
    ]
