from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('all_books', views.all_books, name='all_books'),
    path('delete/<int:book_id>', views.delete_book, name='delete_book'),
    path('edit/<int:book_id>', views.edit_book, name='edit_book')
]
