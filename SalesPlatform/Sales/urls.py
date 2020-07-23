from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.user_list, name='users'),
    path('contacts/', views.contact_list, name='contacts'),
]