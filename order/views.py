from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Photo

def index(request):
    photos = Photo.objects.all()
    return render(request, 'index.html', {'photos': photos})