import json
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import BasicAuthentication
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class Authentication(BasicAuthentication):
  def authenticate(self, request):
    user, _ = super(Authentication, self).authenticate(request)
    login(request, user)
    return user, _
  
@api_view(['POST'])
@csrf_exempt
@permission_classes((AllowAny, ))
@renderer_classes((JSONRenderer, ))
@parser_classes((JSONParser, ))
def auth_view(request, format=None):
  username = request.data['username']
  password = request.data['password']
  if username is None:
    return JsonResponse({
			'error': 'Please provide username'
		}, status=400)
  elif password is None:
    return JsonResponse({
			'error': 'Please provide password'
		}, status=400)
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    return JsonResponse({
			"success": "Logged in successfully"
		})
  return HttpResponseBadRequest({
		'error': 'Invalid username or password'
	}, status=400)
  
@api_view(['GET'])
@permission_classes((AllowAny, ))
@renderer_classes((JSONRenderer, ))
@parser_classes((JSONParser, ))
def check_login(request, format=None):
	if request.user.is_authenticated:
		return JsonResponse({
			"success": "Logged in successfully"
		}, status=201)
	return JsonResponse({
		'error': 'Not logged in'
	}, status=400)