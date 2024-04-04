from django.db import models
from django.contrib.auth.models import User


class User(User):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	confirm_password = models.CharField(max_length=100)