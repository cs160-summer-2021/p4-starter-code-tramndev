# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def variant2(request):
    return render(request, 'draw/variant2.html')

def path(request):
    return render(request, 'draw/path.html')