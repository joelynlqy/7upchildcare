from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home.html', None)

def explore_grid(request): 
    return render(request, 'explore_grid.html', None)

def explore_list(request):
    return render(request, 'explore_list.html', None) 

def subsidy(request):
    return render(request, 'subsidy.html', None) 

def maps(request):
    return render(request, 'maps.html', None) 
