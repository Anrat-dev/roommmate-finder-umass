# Generated by Django 3.2.19 on 2023-05-22 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webappl', '0005_alter_profile_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='staus',
            new_name='status',
        ),
    ]
