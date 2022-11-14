from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Order
from .forms import OrderForm

def index(request):
    return render(request, 'index.html')

class MakeOrder(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'make_order.html', {
                "order_form": OrderForm()
            }
        )


    def post(self, request, *args, **kwargs):
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid():
            order_form.instance.costumer = request.user.username
            order = order_form.save(commit=False)
            order.save()
        else:
            order_form = OrderForm()

        return render(
            request,
            "index.html",
            {
                "order_form": OrderForm()
            }
        )

