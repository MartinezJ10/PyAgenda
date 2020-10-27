from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('delete/<int:pk>/', views.deleteContact, name='delete'),
]
