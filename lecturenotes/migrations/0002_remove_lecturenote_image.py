# Generated by Django 3.2.7 on 2022-11-07 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturenotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturenote',
            name='image',
        ),
    ]
