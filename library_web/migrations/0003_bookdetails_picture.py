# Generated by Django 5.1.3 on 2024-11-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_web', '0002_bookdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
    ]
