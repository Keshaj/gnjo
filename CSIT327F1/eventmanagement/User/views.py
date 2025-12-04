#User/views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View function for the index page
    Renders the index.html template
    """
    return render(request, 'User/index.html')

def login_view(request):
    """
    View function for the login page
    Renders the login.html template
    """
    return render(request, 'User/login.html')