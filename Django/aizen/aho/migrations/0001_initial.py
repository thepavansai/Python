# Generated by Django 4.2.7 on 2023-11-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phn', models.IntegerField()),
                ('ad', models.CharField(max_length=20)),
                ('np', models.CharField(max_length=10)),
            ],
        ),
    ]
