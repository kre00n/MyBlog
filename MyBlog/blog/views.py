from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
def aboutme(request):
    return render(request, 'aboutme.html')
def games(request):
    return render(request, 'games.html')
def background(request):
    return render(request, 'background.html')
def wiki(request):
    return render(request, 'wiki.html')

def mgr(request):
    return render(request, 'mgr.html')
def dmc(request):
    return render(request, 'dmc.html')

def mistral(request):
    return render(request, 'mistral.html')
def monsoon(request):
    return render(request, 'monsoon.html')
def sundowner(request):
    return render(request, 'sundowner.html')
def sam(request):
    return render(request, 'sam.html')
def senator(request):
    return render(request, 'senator.html')
def raiden(request):
    return render(request, 'raiden.html')

def dante(request):
    return render(request, 'dante.html')
def vergil(request):
    return render(request, 'vergil.html')