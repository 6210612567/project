# Generated by Django 4.1.5 on 2023-01-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_authinfo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelforapi',
            name='limit',
            field=models.IntegerField(default=3000, max_length=255),
        ),
        migrations.AddField(
            model_name='channelforapi',
            name='limit_time',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
