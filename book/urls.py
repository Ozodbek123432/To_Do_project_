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
#
# urlpatterns = [
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
# ]