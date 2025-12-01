from django.contrib import admin
from book.models import Genre, Book, Author

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
