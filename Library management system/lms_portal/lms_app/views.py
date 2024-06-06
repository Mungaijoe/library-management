from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.



def home(request):
    return render(request,"home.html",context={"current_tab":"home"})


def add_book(request):
    return render(request,"add_book.html",context={"current_tab":"add_book"})

def books(request):
    return render(request,"add_book.html",context={"current_tab":"books"})

def members(request):
    return render(request,"members.html",context={"current_tab":"members"})

def return_b(request):
    return render(request,"return_b.html",context={"current_tab":"return_b"})


def issue(request):
    return render(request,"issue.html",context={"current_tab":"issue"})

def readers(request):
    readers = reader.objects.all()
    return render(request,"readers.html",context={"current_tab": "readers","readers":readers})

def save_reader(request):
    reader_item = reader(
                         reference_id=request.POST['reader_reference_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST['reader_address'],
                         active=True

                         )
    reader_item.save()
    return redirect('/readers')

def add(request):
    book_item = Book(
                     title=request.POST['book_title'],
                     author=request.POST['book_author'],
                     summary=request.POST['book_summary'],
                     isbn=request.POST['book_isbn'],
                     active=True

    )
    book_item.save()
    return redirect('/add_book')
    return render(request, "add_book.html", context={"current_tab": "add_book", "add_book": add_book})


def viewbooks(request):
    books = Book.objects.all()
    return render(request,"viewbooks.html",context={"current_tab": "viewbooks","books":books})


def issue(request):
    instances = BookInstance.objects.all()
    return render(request,"issue.html",context={"current_tab": "issue","instances":instances})


def calculate_rent_fee(due_back, return_date):

    if due_back and return_date > due_back:
        days_late = (return_date - due_back).days
        return days_late * 10
    return 0

def return_book(book_instance_id):
    try:
        book_instance = BookInstance.objects.get(id=book_instance_id)
        readers = reader.objects.get(reader_name=book_instance.reader_name)
        return_date = timezone.now().date()

        rent_fee = book_instance.calculate_rent_fee(return_date)

        reader.outstanding_debt += rent_fee

        if reader.outstanding_debt > 500:
            return f"Cannot return book. Outstanding debt {reader.outstanding_debt} exceeds KES 500."


        book_instance.status = 'a'
        book_instance.due_back = None
        book_instance.save()


        reader.save()

        return f"Book returned successfully. Rent fee charged: KES {rent_fee}. Outstanding debt: KES {reader.outstanding_debt}."
    except BookInstance.DoesNotExist:
        return "Book instance not found."
    except reader.DoesNotExist:
        return "Reader not found."

    return render(request, "return_b.html", context={"current_tab": "return"})

