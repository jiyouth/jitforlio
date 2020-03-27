from django.shortcuts import render

# Create your views here.

def youtube(request):
    return render(request, 'jitforlio/youtube.html')

def visualdesign(request):
    return render(request, 'jitforlio/visualdesign.html')

def home(request):
    return render(request, 'jitforlio/home.html')
