# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:room_name>/', views.room, name='room'),

    path('variant1', views.variant1, name='variant1'),
    path('variant2', views.variant2, name='variant2'),
]

