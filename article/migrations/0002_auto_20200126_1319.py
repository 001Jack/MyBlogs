# Generated by Django 2.2.1 on 2020-01-26 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id']},
        ),
    ]