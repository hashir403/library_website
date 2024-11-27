from django.db import models


class Employee(models.Model):
    uname = models.CharField(max_length=30)
    uemail = models.EmailField()
    upassword = models.CharField(max_length=30)


class Bookdetails(models.Model):
    bookName = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    publicationDate = models.DateField()
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='book_images/', blank=True, null=True)
    book = models.FileField(upload_to='book_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.bookName
    


        