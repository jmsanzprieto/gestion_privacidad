# Generated by Django 3.2.12 on 2024-02-11 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contraseñas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contraseñas',
            old_name='password',
            new_name='encrypted_password',
        ),
    ]
