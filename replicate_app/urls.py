# replicate_app/urls.py
from django.urls import path
from .views import replicate_view

urlpatterns = [
    path('v1/replicate/', replicate_view),
]