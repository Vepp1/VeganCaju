from django.contrib import admin
from .models import Order
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Order)
class OrderAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('size', 'flavor', 'status', 'created_on', 'pick_up')
    search_fields = ['size', 'created_on', 'id']
