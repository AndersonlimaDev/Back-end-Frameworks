from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('patch/<str:id>/', views.patch, name='patch'),
    path('delete/<str:id>/', views.delete, name='delete'),
]

