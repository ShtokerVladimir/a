from django.urls import path
from .views import index

app_name = 'frontend'

urlpatterns = [
	path('', index, name='index'),
	path('new-test', index, name='index'),
	path('last-test', index, name='index'),
	path('all-test', index, name='index'),
	path('login', index, name='login'),
]
