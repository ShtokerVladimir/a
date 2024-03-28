from django.urls import path
from .views import home, contact
from . import views



urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]

