# Generated by Django 4.1.13 on 2024-06-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0005_testimonial_profession_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='profession',
            field=models.CharField(max_length=200),
        ),
    ]
