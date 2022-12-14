from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error_page, name='error_page'),
    path('make_order/', views.MakeOrder.as_view(), name='make_order'),
    path('my_orders/', views.OrderList.as_view(), name='my_orders'),
    path('edit_order/<int:id>/', views.EditOrder.as_view(), name='edit_order'),
    path('delete_order/<int:id>/', views.DeleteOrder.as_view(), name='delete_order'),
]