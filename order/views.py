from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View

def home_page(request):
    return render(request, 'index.html')