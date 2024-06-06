from django.test import TestCase
from .models import reader, Book, BookInstance
from django.urls import reverse
from datetime import date
# Create your tests here.
class ReaderModelTest(TestCase):
    def setUp(self):
        self.reader = reader.objects.create(
            reference_id='12345',
            reader_name='John Doe',
            reader_contact='1234567890',
            reader_address='Nairobi',
            active=True
        )

    def test_reader_creation(self):
        self.assertEqual(self.reader.reader_name, 'John Doe')
        self.assertEqual(self.reader.__str__(), 'John Doe')
        self.assertTrue(self.reader.active)


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Django',
            author='Joe Mungai',
            summary='Intro to Django.',
            isbn='1234567890123',
            active=True
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Django')
        self.assertEqual(self.book.__str__(), 'Django')
        self.assertTrue(self.book.active)




class BookInstanceModelTest(TestCase):
    def setUp(self):
        self.book_instance = BookInstance.objects.create(
            reader_name='John Doe',
            title='Django',
            author='Joe Mungai',
            due_back=date(2024, 12, 31),
            status='o'
        )

    def test_book_instance_creation(self):
        self.assertEqual(self.book_instance.reader_name, 'John Doe')
        self.assertEqual(self.book_instance.title, 'Django')
        self.assertEqual(self.book_instance.__str__(), 'o (Django)')
        self.assertEqual(self.book_instance.status, 'o')
        self.assertEqual(self.book_instance.due_back, date(2024, 12, 31))

    def test_book_instance_ordering(self):
        book_instance_2 = BookInstance.objects.create(
            reader_name='Jane Doe',
            title='Learning Django',
            author='James ',
            due_back=date(2024, 6, 30),
            status='a'
        )
        book_instances = BookInstance.objects.all()
        self.assertEqual(book_instances[0], book_instance_2)
        self.assertEqual(book_instances[1], self.book_instance)
