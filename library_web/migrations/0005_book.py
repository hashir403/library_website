# Generated by Django 5.1.3 on 2024-11-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_web', '0004_rename_authername_bookdetails_bookname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('file_path', models.CharField(max_length=500)),
            ],
        ),
    ]
