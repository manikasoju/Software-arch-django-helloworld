from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_world(request):
    data = {"Message": "Hello World!"}
    return JsonResponse(data)

