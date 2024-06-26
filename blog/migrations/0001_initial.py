# Generated by Django 4.1.13 on 2024-06-25 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('author_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('title', models.CharField(max_length=200)),
                ('blog_desc', models.TextField()),
                ('image', models.ImageField(default='defaultpost.jpg', upload_to='post_pics')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_by', models.CharField(max_length=100)),
                ('commenter_email', models.EmailField(max_length=254)),
                ('commenter_website', models.CharField(max_length=100)),
                ('comment_desc', models.CharField(max_length=300)),
                ('commenter_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replied_by', models.CharField(max_length=100)),
                ('reply_desc', models.CharField(max_length=300)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='blog.comment')),
            ],
        ),
    ]