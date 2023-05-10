from django.db import models

# Create your models here.
import uuid
from service.models import Service


class Payement(models.Model):

    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="orderr")

    payement_id = models.CharField(max_length=100)
    payement_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.payement_id


class Order(models.Model):

    STATUS = {
        ('New', 'New'),
        ('Accepted', 'accepted'),
        ('Completed', 'Completed'),
        ('Cenceled', 'Cenceled'),

    }

    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="orderrr")

    payement = models.ForeignKey(
        Payement, on_delete=models.SET_NULL, blank=True, null=True)

    order_number = models.CharField(max_length=20)

    wilaya = models.CharField(max_length=50)

    adress_line_1 = models.CharField(max_length=50)

    adress_line_2 = models.CharField(max_length=50, blank=True)

    state = models.CharField(max_length=50)

    city = models.CharField(max_length=50)

    order_note = models.CharField(max_length=100, blank=True)

    order_total = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.wilaya


class OrderService(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="orderrre")

    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

    user = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="orderrree")

    ordered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.service.Service_name
