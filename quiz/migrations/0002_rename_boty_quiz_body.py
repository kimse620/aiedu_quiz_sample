# Generated by Django 3.2.5 on 2021-07-11 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='boty',
            new_name='body',
        ),
    ]
