# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),


    # Deliverable 3.9 @Tram Nguyen & Hiroshi Usui  
    path('new_interaction', views.new_interaction, name='new_interaction'),
]

