from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,"generator/home.html", {'password' : 'hellopython'})


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("special"):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get("numbers"):
        characters.extend(list('012345678'))


    length = int(request.GET.get('length', 8))

    thep = ''

    for x in range(length):
        thep += random.choice(characters)
    return render(request,"generator/password.html", {'password' : thep})
