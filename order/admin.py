from django.contrib import admin

# Register your models here.
from .models import Payement, Order, OrderService

admin.site.register(Payement)
admin.site.register(Order)
admin.site.register(OrderService)
