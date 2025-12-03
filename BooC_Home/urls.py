# book/urls.py  (yoki login_app/urls.py)
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from book.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # ← LOGIN
    TokenRefreshView,       # ← yangi access token olish
)

urlpatterns = [
    #===================  admin =====================
     path('admin/', admin.site.urls,name='admin'),

    # ===================login======================

    path('api/token/', TokenObtainPairView.as_view(), name='login qilish'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='logo qilish'),

    # ===================== GENRE =====================

    path('genres/', GenreListView.as_view(), name='korish'),
    path('genres/create/', GenreCreateView.as_view(), name='korish'),

    # ======================BOOC ==========================

    path('book/', BookDataGetView.as_view(), name='yangilash'),
    path('book/create/', BookDataCreateView.as_view(), name='korish'),
    path('book/<int:pk>/', BookDataPutAndPatch.as_view(), name='ozgartish'),
    path('book/<int:pk>/delete/',BookDataDeleteView.as_view(), name='ooxhrish'),

    # ===================== AUTHOR =====================

    path('authors/', AuthorDataGetView.as_view(), name='korish'),
    path('authors/create/', AuthorDataCreateView.as_view(), name='yangilash'),
    path('authors/<int:pk>/', AuthorDataPutAndPatch.as_view(), name='ozgartish'),
    path('authors/<int:pk>/delete/', AuthorDataDeleteView.as_view(), name='ooxhrish'),  #
]