# Generated by Django 3.2.7 on 2022-11-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
