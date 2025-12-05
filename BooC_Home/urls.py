# book/urls.py  (yoki login_app/urls.py)
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from book.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    #===================  admin =====================
     path('admin/', admin.site.urls,name='admin'),

    # ===================login======================

    path('api/token/', TokenObtainPairView.as_view(), name='login qilish'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='logo qilish'),
    path('menu/', include("book.urls")),

]