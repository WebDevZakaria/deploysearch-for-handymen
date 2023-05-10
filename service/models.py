from email.policy import default
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

import uuid


class Wilaya(models.Model):

    wilaya_name = models.CharField(max_length=200)

    wilaya_matricule = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.wilaya_name


class baladiya(models.Model):

    baladiya_name = models.CharField(max_length=200)

    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.baladiya_name


class Category(models.Model):

    Category_name = models.CharField(max_length=200)

    description_cat = models.TextField(max_length=500, blank=True)

    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    baladiya = models.ForeignKey(baladiya, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.Category_name


class Service(models.Model):

    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="Sevice")

    Service_name = models.CharField(max_length=200)

    description = models.TextField(max_length=500, blank=True)

    image = models.ImageField(upload_to='photos/Service')

    is_avalaible = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    baladiya = models.ForeignKey(baladiya, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.category.wilaya.wilaya_name


class Createservice(models.Model):

    user = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="Sev")

    Service_name = models.CharField(max_length=200)

    description = models.TextField(max_length=500, blank=True)

    images = models.ImageField(upload_to='photos/Ser')

    your_sertificate = models.ImageField(upload_to='photos/Competence')

    is_avalaible = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    baladiya = models.ForeignKey(baladiya, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):

        return self.category.wilaya.wilaya_name


class ReviewRating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        "accounts.Account", models.CASCADE, related_name="Sevicess")
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)

    status = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'service']]

    def __str__(self):

        return self.owner.email
