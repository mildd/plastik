# Generated by Django 2.2.5 on 2019-09-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190910_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]