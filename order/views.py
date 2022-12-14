from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Order
from .forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


def error_page(request):
    return render(request, '404.html')

class MakeOrder(LoginRequiredMixin, View):


    def get(self, request, *args, **kwargs):
        return render(request, 'make_order.html', {
                "order_form": OrderForm()
             }
         )


    def post(self, request, *args, **kwargs):
        order_form = OrderForm(data = request.POST)
        if order_form.is_valid():
            order_form.instance.costumer = request.user.username
            order = order_form.save(commit = False)
            order.save()
            messages.add_message(request, messages.SUCCESS, "Order complete")
            return render(
            request,
            "index.html",
             {
                "order_form": OrderForm()
             }
         )
        else:
            order_form = OrderForm()
            messages.add_message(request, messages.ERROR, 
            "Please, choose at date at least 3 days from now")
            return render(
            request,
            "make_order.html",
             {
                "order_form": OrderForm()
             }
         )
      


class GetOrder():
    def get_user_order(self, request, id):
        costumer = request.user.username
        queryset =  Order.objects.filter(costumer = costumer)
        return get_object_or_404(queryset, id = id)


class OrderList(generic.ListView, LoginRequiredMixin):
        model = Order
        template_name = "my_orders.html"
        paginate_by = 3


        def get_queryset(self):
            return Order.objects.filter(costumer = self.request.user.username)


class EditOrder(LoginRequiredMixin, GetOrder, View):


    def get(self, request, id, *args, **kwargs):
        order = self.get_user_order(request, id)
        if order.status == 0:
            return render(request, "edit_order.html", 
    {"order_form": OrderForm(instance = order),
            "order": order}
         )
        else:
            return render(request, "404.html")


    def post(self, request, id, *args, **kwargs):
        order = self.get_user_order(request, id)
        order_form = OrderForm(data = request.POST)
        if order_form.is_valid():
                order.size = order_form.cleaned_data['size']
                order.flavor = order_form.cleaned_data['flavor']
                order.pick_up = order_form.cleaned_data['pick_up']
                orderform = order_form.save(commit = False)
                orderform.save()
                order.save()
                messages.add_message(request, messages.SUCCESS, 
        "Order Updated!")
                return redirect('my_orders')
        else:
                order_form = OrderForm()
                messages.add_message(request, messages.ERROR, 
        "Please, choose at date at least 3 days from now")

        return render(
            request,
            "edit_order.html",
             {
                "order_form": OrderForm()
             }
         )


class DeleteOrder(LoginRequiredMixin, GetOrder, View):


    def get(self, request, id, *args, **kwargs):
        order = self.get_user_order(request, id)
        if order.status == 0:
            order.delete()
            messages.add_message(request, messages.SUCCESS, "Order Deleted!")
        else:
            return render(request, "404.html")
  
        return redirect('my_orders')


