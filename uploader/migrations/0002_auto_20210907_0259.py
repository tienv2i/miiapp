# Generated by Django 3.2.7 on 2021-09-07 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='description',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='uploaded_at',
            new_name='uploaded',
        ),
    ]