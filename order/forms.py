from django import forms
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):

    class Meta:

        model = Order

        fields = ['adress_line_1',

                  'adress_line_2', 'state', 'city', 'order_note']
