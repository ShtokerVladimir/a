from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    context = {
        'title': 'Домашняя страница',
    }
    return render(request, 'prototype/home.html', context)


def contact(request):
    context = {
        'title': 'Страница контактов',
    }
    return render(request, 'prototype/contact.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'prototype/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


