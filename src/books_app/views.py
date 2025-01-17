from django.shortcuts import render
from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books_app/book_list.html"
