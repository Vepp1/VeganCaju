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


class ViewOrder(View):

    def get(self, request, *args, **kwargs):
        costumer = request.user.username
        queryset = Order.objects.filter(costumer=costumer)

        return render(
            request,
            "my_orders.html", {'queryset': queryset}
        )

    
class EditOrder(View):

    def get(self, request, id, *args, **kwargs):
        costumer = request.user.username
        queryset = Order.objects.filter(costumer=costumer)
        order = get_object_or_404(queryset, id=id)

        return render(
            request,
            "edit_order.html", {"order_form": OrderForm(instance=order),
            "order": order}
        )

    def post(self, request, id, *args, **kwargs):
        order_form = OrderForm(data=request.POST)
        costumer = request.user.username
        queryset = Order.objects.filter(costumer=costumer)
        order = get_object_or_404(queryset, id=id)
        if order_form.is_valid():
            order.size = order_form.cleaned_data['size']
            order.flavor = order_form.cleaned_data['flavor']
            order.pick_up = order_form.cleaned_data['pick_up']
            orderform = order_form.save(commit=False)
            orderform.save()
            order.save()
            return redirect('my_orders')
        else:
            order_form = OrderForm()

        return render(
            request,
            "index.html",
            {
                "order_form": OrderForm()
            }
        )
