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

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'admin-details/',
        views.admin_details,
        name='admin_details'
    ),

    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),
]