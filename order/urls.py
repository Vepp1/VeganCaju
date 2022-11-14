from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('make_order/', views.MakeOrder.as_view(), name='make_order'),
]