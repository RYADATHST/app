# Generated by Django 4.2.1 on 2023-05-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domaine',
            old_name='name',
            new_name='createddate',
        ),
    ]
