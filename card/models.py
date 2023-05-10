from django.db import models

from service.models import Service


import uuid
# Create your models here.


class CardItems(models.Model):

    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="Servicce")

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    totals = models.FloatField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
