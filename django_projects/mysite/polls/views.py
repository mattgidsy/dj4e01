from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index, e84eae17.")

def owner(request):
   return HttpResponse("Hello, world. 5a77cde0 is the polls index.")