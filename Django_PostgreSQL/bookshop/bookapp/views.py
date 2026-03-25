from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect
from .forms import BookForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book(
                name = form.cleaned_data['book_name'],
                price = form.cleaned_data['book_price']
            )
            book.save()
            return HttpResponseRedirect('all_books')

    form = BookForm()
    return render(request, 'bookapp/index.html', {
        'bookForm':form
    })

def all_books(request):
    books = Book.objects.all()
    return render(request, 'bookapp/all_books.html', {
        'books': books
    })

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('all_books')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.name = request.POST['book-name']
        book.price = request.POST['book-price']
        book.save()
        return redirect('all_books')
    return render(request, 'bookapp/editbook.html', {
        'book':book
    })





















# Stará funkce
    # if request.method == 'POST':
    #     book_name = request.POST['book-name']
    #     book_price = request.POST['book-price']
    #     Book.objects.create(
    #         name= book_name,
    #         price= book_price
    #     )
    #     return HttpResponseRedirect('all_books')
    # return render(request, 'bookapp/index.html')