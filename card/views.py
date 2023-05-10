from django.shortcuts import render, redirect
# Create your views here.
from service.models import Service

from.models import CardItems


def card(request):

    if request.user.is_authenticated:

        cartitem = CardItems.objects.filter(owner=request.user)

    else:

        cartitem = None

    context = {"cartitem": cartitem}

    return render(request, 'cards/Cardpage.html', context)


def addtocard(request, pk):

    services = Service.objects.get(id=pk)

    user = request.user

    try:
        card = CardItems.objects.get(owner=user, service=services)
        card.totals = card.totals + 1
        card.save()
        return redirect("cart")

    except:

        cart = CardItems.objects.create(owner=user, service=services)

        cart.save()

    return redirect("cart")


def cardremove(request, pk):

    cartitem = CardItems.objects.get(id=pk)

    cartitem.delete()
    
    return redirect("cart")

