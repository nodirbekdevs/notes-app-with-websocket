from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notes, name='get_notes'),
    path('count/', views.get_note_count, name='get_note_count'),
    path('<int:pk>/', views.get_note, name='get_note'),
    path('make/', views.make_note, name='make_note'),
    path('edit/<str:pk>/', views.update_note, name='update_note'),
    path('delete/<str:pk>/', views.delete_note, name='update_note'),
]
