from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_template, name='UserTemplate'),
    path('contact/', views.contacts_template, name='ContactTemplate'),
    path('enterContent/',views.EnterContent,name='EnterContent'),
    path('apidocs/',views.APIdocs,name='APIdocs'),

]