from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tarefas/', views.task_list, name='task_list'),
    path('tarefas/<int:pk>/', views.task_detail, name='task_detail'),
]
