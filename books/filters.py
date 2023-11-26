import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'name' : ['icontains'] ,
             'description' :['icontains'],
             'title':['icontains'],
             'author':['icontains'],
             'publication_year':['lt','gt'],
        }