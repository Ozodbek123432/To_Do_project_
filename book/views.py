from .models import Genre, Author, Book
from .serializers import AuthorData, BookData, GenreData
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework.exceptions import NotFound


# ==================== AUTHOR ====================

class AuthorDataCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AuthorDataGetView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorData
    permission_classes = [AllowAny]

class AuthorDataPutAndPatch(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AuthorDataDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# ==================== GENRE ====================

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreData
    permission_classes = [AllowAny]

class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreData
    permission_classes = [IsAdminUser]

# ==================== BOOK ====================

class BookDataCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class BookDataGetView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookData
    permission_classes = [AllowAny]

class BookDataPutAndPatch(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class BookDataDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookData
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]