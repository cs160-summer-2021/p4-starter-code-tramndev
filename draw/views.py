# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })


# Deliverable 3.9 @Tram Nguyen & Hiroshi Usui  
def new_interaction(request):
    return render(request, 'draw/new_interaction.html')