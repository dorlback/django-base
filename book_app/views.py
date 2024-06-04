from django.shortcuts import render
from django.views.generic.list import ListView
from book_app.models import Author, Book

class BookListView(ListView):
    model = Book
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context