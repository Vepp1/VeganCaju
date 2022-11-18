from django import forms
from .models import Order

class DateInput(forms.DateInput):
        input_type = 'date' 

class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ('size', 'flavor', 'pick_up')
        widgets = {
            'pick_up': DateInput(),
        }