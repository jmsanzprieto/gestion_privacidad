# Generated by Django 3.2.12 on 2024-02-11 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contraseñas', '0002_rename_password_contraseñas_encrypted_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contraseñas',
            old_name='encrypted_password',
            new_name='password',
        ),
    ]
