# Generated by Django 3.2.7 on 2022-11-07 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lecturenotes', '0002_remove_lecturenote_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturenote',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]