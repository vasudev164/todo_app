from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.show_todo_list, name='show_todo_list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
]
