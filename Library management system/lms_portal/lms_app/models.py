from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200 , help_text="enter id")
    reader_name=models.CharField(max_length=200)
    reader_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)
    outstanding_debt = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)





class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(default='',max_length=200)
    summary = models.TextField(default='', max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')

    active = models.BooleanField(default=True)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])



class BookInstance(models.Model):
    reader_name=models.CharField(default='',max_length=200)
    title = models.CharField(default='',max_length=200)
    author=models.CharField(default='',max_length=200)
    due_back = models.DateField(null=True, blank=True)


    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):

        return f'{self.status} ({self.title})'

