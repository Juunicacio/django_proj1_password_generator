from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, 'generator/index.html', {'password': '873oeuqwfgr'})

def eggs(request): # test path function
    return HttpResponse ('Example page that talk about eggs')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    # check if the user wants the uppercase checkbox on
    if request.GET.get('uppercase'):
	    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    # check if the user wants the special checkbox on
    if request.GET.get('special'):
	    characters.extend(list('!@#$%&*'))
    
    # check if the user wants the numbers checkbox on
    if request.GET.get('numbers'):
	    characters.extend(list('0123456789'))

    # information from the dropdown named 'length'
    length = int(request.GET.get('length'))

    thepassword = ''    
    for x in range(length):
	    thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')