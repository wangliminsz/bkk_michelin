# Generated by Django 4.0.1 on 2022-01-26 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbot_app', '0004_rename_mbcontact_mbkk_mbfoodstyle_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mbkk',
            new_name='mbkkstyle',
        ),
    ]