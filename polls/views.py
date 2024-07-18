from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. My first view I might add :)


def index(request):
   return HttpResponse("Greetings human, you have arrived at my polls site.")

    