# Generated by Django 4.1.5 on 2023-01-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_animal_info_desease_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal_info',
            old_name='desease_update',
            new_name='desease_updated',
        ),
    ]