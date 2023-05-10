from django.contrib import admin

# Register your models here.

from.models import Service, Category, Wilaya, Createservice, ReviewRating, baladiya


admin.site.register(Wilaya)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Createservice)
admin.site.register(ReviewRating)
admin.site.register(baladiya)
