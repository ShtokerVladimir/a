from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, FileForm, BirthdayGreeterForm
from rest_framework.views import View
from rest_framework.renderers import TemplateHTMLRenderer
from django.conf import settings
from requests import post
from .tasks import run_bot
from django.urls import reverse

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
        return redirect('login')
    
    context = {
        'title': 'Home Page',
        'form': form
    }
    return render(request, 'prototype/home.html', context=context)

def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        context = {
            'title': 'Contacts Page',
        }
        return render(request, 'prototype/contact.html', context=context)

def login_view(request):
    title = "Login Page"
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
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

# def register_view(request):
#     title = 'Register Page'
#     if request.user.is_authenticated:
#         return redirect('home')
#     elif request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             save_form = form.save(commit=False)
#             save_form.set_password(form.cleaned_data['password'])
#             save_form.save()
#             messages.success(request=request, message='You have successfully registered')
#             return redirect('register')
#         else:
#             context = {
#                 'title': title,
#                 'form': form
#             }
#             return render(request, 'prototype/register.html', context=context)
#     return render(request, 'prototype/register.html', context=context)

# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     elif request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             password = form.data.get('password')
#             confirm_password = form.data.get('confirm_password')
#             if password != confirm_password:
#                 send_telegram_message(settings.API_TOKEN, settings.CHAT_ID, 'Passwords do not match')
#             messages.success(request=request, message='You have successfully registered')
#             return redirect('register')
#         else:
#             messages.error(request=request, message='Invalid data')
#     else:
#         form = RegisterForm()
        
#     context = {
#         'title': 'Register Page',
#         'form': form
#     }
#     return render(request, 'prototype/register.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')

def history_test(request):
    context = {
        'title': 'History of the tests'
    }
    return render(request, 'prototype/history_test.html', context=context)

def new_test(request):
    context = {
        'title': 'New tests'
    }
    return render(request, 'prototype/new_test.html', context=context)

def test(request):
    context = {
        'title': 'Test Page',
    }
    return render(request, 'prototype/test.html', context=context)

def success_view(request):
    context = {
        'title': 'Success Page',
    }
    return render(request, 'success.html', context=context)
