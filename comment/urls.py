from django.urls import path
from . import views

urlpatterns = [
    path('', views.commentResearchPage, name='commentresearchpage'),
    path('create', views.commentCreatePage, name='commentcreatepage'),
]
