from django.shortcuts import render

# Create your views here.
def home(request):
    """The home page."""
    return render(request, 'pages/home.html')

def page1(request):
    """Page 1."""
    return render(request, 'pages/page1.html')

def google(request):
    """Google source code."""
    return render(request, 'pages/google.html')