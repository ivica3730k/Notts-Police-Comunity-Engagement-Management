# Generated by Django 3.0.2 on 2020-02-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='isCommunityManager',
            field=models.BooleanField(default=False),
        ),
    ]
