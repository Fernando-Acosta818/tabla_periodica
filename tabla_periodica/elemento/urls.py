from django.urls import path
from . import views

urlpatterns = [
    path('<str:elem>', views.elemento)
]