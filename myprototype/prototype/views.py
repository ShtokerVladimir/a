from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, FileForm
from rest_framework.views import View
from rest_framework.renderers import TemplateHTMLRenderer

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.data.get('file')
                type = form.data.get('type')
                print(file, type)
                messages.error(request, 'No such service yet!')
            else:
                messages.error(request, 'Invalid file')
        else:
            form = FileForm()
    else:
        form = None
    
    context = {
        'title': 'Home Page',
        'form': form
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


