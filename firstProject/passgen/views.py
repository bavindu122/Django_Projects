from django.shortcuts import render , HttpResponse
import random
from django.http import JsonResponse 


# Create your views here.

def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list('')
    password = ''
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('lowercase'):
        char.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()-+'))
    length = int(request.GET.get('length',12))
    for i in range(length):
        password += random.choice(char)
    data = {
        'password': password
    }
    return render(request, 'passgen.html', data)
