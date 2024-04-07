from django.urls import include, path
from .views import auth_view, check_login

urlpatterns = [
	path('auth/login', auth_view, name='auth_view'),
	path('auth/check', check_login, name='check_login'),
]
