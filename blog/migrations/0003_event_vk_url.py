# Generated by Django 2.2.5 on 2019-09-08 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='vk_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]