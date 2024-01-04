# backend/urls.py

from django.urls import path
from .views import generate_image

urlpatterns = [
    path('api/generate_image/', generate_image, name='generate_image'),

]
