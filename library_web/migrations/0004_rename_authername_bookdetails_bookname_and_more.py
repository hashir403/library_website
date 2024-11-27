# Generated by Django 5.1.3 on 2024-11-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_web', '0003_bookdetails_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdetails',
            old_name='autherName',
            new_name='bookName',
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='book',
            field=models.FileField(blank=True, null=True, upload_to='book_pdfs/'),
        ),
    ]
