# # login_app/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     AuthorListCreateView,
#     AuthorDetailView,
#     GenreListView,
#     GenreCreateView,
#     GenreUpdateView,
#     BookModelViewSet
# )
#
# # ModelViewSet uchun router
# router = DefaultRouter()
# router.register(r'books', BookModelViewSet, basename='book')
from django.urls import path
from book.views import *
urlpatterns = [

# ===================== GENRE =====================

path('genres/', GenreListView.as_view(), name='korish'),
path('genres/create/', GenreCreateView.as_view(), name='korish'),

# ======================BOOC ==========================

path('book/', BookDataGetView.as_view(), name='yangilash'),
path('book/create/', BookDataCreateView.as_view(), name='korish'),
path('book/<int:pk>/', BookDataPutAndPatch.as_view(), name='ozgartish'),
path('book/<int:pk>/delete/', BookDataDeleteView.as_view(), name='ooxhrish'),

# ===================== AUTHOR =====================

path('authors/', AuthorDataGetView.as_view(), name='korish'),
path('authors/create/', AuthorDataCreateView.as_view(), name='yangilash'),
path('authors/<int:pk>/', AuthorDataPutAndPatch.as_view(), name='ozgartish'),
path('authors/<int:pk>/delete/', AuthorDataDeleteView.as_view(), name='ooxhrish'),  #
#     # Author — APIView
#     path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
#     path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
#
#     # Genre — GenericAPIView
#     path('genres/', GenreListView.as_view(), name='genre-list'),
#     path('genres/create/', GenreCreateView.as_view(), name='genre-create'),
#     path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name='genre-update'),
#
#     # Book — ModelViewSet (router orqali)
#     path('', include(router.urls)),  # → /books/, /books/1/, ...
]