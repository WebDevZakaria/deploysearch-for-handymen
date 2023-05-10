from django.contrib import admin

# Register your models here.

from .models import Account, Message


admin.site.register(Account)


admin.site.register(Message)
