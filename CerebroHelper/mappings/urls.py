from django.urls import path
from . import views

urlpatterns = [
    path('', views.mappings, name='mappings'),
]