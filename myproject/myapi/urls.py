from django.urls import path
from myapi import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
]