from django.urls import path
from . import views

urlpatterns = [
    path('', views.memorybook, name='memorybook'),
    path('create', views.memoryCreate, name='memorycreate'),
]
