from django.urls import path
from . import views

urlpatterns = [
    path('userT/', views.user_template, name='UserTemplate'),
    path('contactT/', views.contacts_template, name='ContactTemplate'),

]