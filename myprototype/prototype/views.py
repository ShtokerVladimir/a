from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from rest_framework.views import View
from rest_framework.renderers import TemplateHTMLRenderer

def home(request):
    context = {
        'title': 'Home Page',
    }
    return render(request, 'prototype/home.html', context=context)

def contact(request):
    context = {
        'title': 'Contacts Page',
    }
    return render(request, 'prototype/contact.html', context=context)

def login_view(request):
    title = "Login Page"
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                form.full_clean()
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                form.full_clean()
                return redirect('login')
    else:
        form = LoginForm()
    
    context = {
        'title': title,
        'form': form
    }
    
    return render(request, 'prototype/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')


