from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Order
# from .forms import OrderForm

def index(request):
    return render(request, 'index.html')

class MakeOrder(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'make_order.html')

