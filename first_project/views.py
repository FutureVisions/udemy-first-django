from django.shortcuts import render
from . import machine_learning

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    user_input = request.GET['user_input']
    user_input = machine_learning.multiply(user_input)
    return render(request, 'result.html', {'home_input': user_input})