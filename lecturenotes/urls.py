from django.urls import path
from . import views

urlpatterns = [
    path('', views.lectureNotes, name='notespage'),
    path('create/', views.lectureNoteCreate, name='notecreate'),
]
