from .models import (Genre, Author, Book)
from rest_framework import serializers

# ==================== AUTHOR ====================

class AuthorData(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

# ==================== GENRE ====================

class GenreData(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields ="__all__"

# ==================== BOOK ====================

class BookData(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"