# Generated by Django 4.1.13 on 2024-06-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
