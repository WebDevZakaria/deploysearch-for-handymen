from os import link
from .models import Wilaya


def wilaya(request):

    links = Wilaya.objects.all()

    return dict(links=links)
