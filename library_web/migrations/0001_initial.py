# Generated by Django 5.1.3 on 2024-11-19 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('uemail', models.EmailField(max_length=254)),
                ('upassword', models.CharField(max_length=30)),
            ],
        ),
    ]
