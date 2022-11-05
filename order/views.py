from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Order

def index(request):
    return render(request, 'index.html')

def make_order(request):
    return render(request, 'make_order.html')

