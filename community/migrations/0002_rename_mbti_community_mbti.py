# Generated by Django 3.2.13 on 2022-12-07 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='MBTI',
            new_name='mbti',
        ),
    ]
