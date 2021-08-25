from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, 'index.html', {})


# @login_required
def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name,
        'username': request.user.username,
    })
