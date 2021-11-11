from typing import Sequence
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    thepassword=""
    length = int(request.GET.get('length'))
    choices = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase') == 'on':
        choices.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers') == 'on':
        choices.extend(list('0123456789'))
    if request.GET.get('special') == 'on':
        choices.extend(list('!@#$%^&*()[]/'))

    for i in range(length):
        thepassword+=random.choice(choices)
    
    return render(request, 'generator/password.html', {'password':thepassword})