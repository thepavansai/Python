# Generated by Django 4.2.7 on 2023-11-26 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plannet', '0002_staff_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='namei',
        ),
    ]