# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

# def room(request, room_name):
#     return render(request, 'draw/room.html', {
#         'room_name': room_name
#     })

def variant1(request):
    return render(request, 'draw/variant1.html')

def variant2(request):
    return render(request, 'draw/variant2.html')