from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notes, name='get_notes'),
    path('<int:pk>/', views.get_note, name='get_note'),
]