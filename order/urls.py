from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.make_order, name='make_order'),
]