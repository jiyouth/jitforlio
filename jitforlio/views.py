from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'jitforlio/home.html')

def visualdesign(request):
    return render(request, 'jitforlio/visualdesign.html')

def youtube(request):
    return render(request, 'jitforlio/visualdesign.html')