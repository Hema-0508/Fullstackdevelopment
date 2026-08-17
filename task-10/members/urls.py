from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),

    path('members/', views.members, name='members'),

    path(
        'members/details/<int:id>',
        views.details,
        name='details'
    ),

    path('todo/', views.todo, name='todo'),

    path(
        'todo/update/<int:id>/',
        views.update_todo,
        name='update_todo'
    ),

    path(
        'todo/delete/<int:id>/',
        views.delete_todo,
        name='delete_todo'
    ),
]