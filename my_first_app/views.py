from django.views.generic import TemplateView
from django.shortcuts import render

from my_first_app.models import Book


# Create your views here.
def index(request):
    cars = [
        {
            "made": "Toyota",
            "model": "Corolla",
            "year": 2015,
            "color": "red",
            "price": 5000
        },
        {
            "made": "Kia",
            "model": "Rio",
            "year": 2016,
            "color": "blue",
            "price": 6000
        }
    ]

    context = {
        "cars": cars
    }
    return render(request, 'index.html', context)


def books(request):
    books_query = Book.objects.all()
    context = {
        "books": books_query
    }
    return render(request, 'books.html', context)


class BooksView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


def book(request, book_id):
    book_query = Book.objects.get(id=book_id)
    context = {
        "book": book_query
    }
    return render(request, 'book.html', context)
