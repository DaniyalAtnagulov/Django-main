# Generated by Django 5.0.1 on 2024-02-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw4_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]
