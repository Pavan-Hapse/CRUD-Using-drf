# Generated by Django 4.1.5 on 2023-01-31 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_rename_desease_update_animal_info_desease_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal_info',
            old_name='desease_updated',
            new_name='desease_update',
        ),
    ]
