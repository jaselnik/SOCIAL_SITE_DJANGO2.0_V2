# Generated by Django 2.0.2 on 2018-03-23 19:29

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofille_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofille',
            managers=[
                ('kirov', django.db.models.manager.Manager()),
            ],
        ),
    ]
