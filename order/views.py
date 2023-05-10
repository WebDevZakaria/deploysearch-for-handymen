from django.shortcuts import render, redirect

# Create your views here.
from datetime import date
from datetime import datetime
from card.models import CardItems
from .models import Order
from .forms import OrderForm

from .models import OrderService


def checkoute(request):

    cartitem = CardItems.objects.filter(owner=request.user)

    orderform = OrderForm()

    if request.method == "POST":

        orderform = OrderForm(request.POST)

        if orderform.is_valid():

            orderforms = orderform.save(commit=False)

            orderforms.owner = request.user

            orderforms.wilaya = request.user.wilaya.wilaya_name

            orderforms.ip = request.META.get('REMOTE_ADDR')

            orderforms.save()

            yr = int(date.today().strftime('%Y'))
            dt = int(date.today().strftime('%d'))
            mt = int(date.today().strftime('%m'))
            d = date(yr, mt, dt)

            current_date = d.strftime("%Y%m%d")

            order_number = current_date + str(orderforms.id)

            orderforms.order_number = order_number

            orderforms.save()

            order = Order.objects.get(order_number=order_number)

            context = {"order": order, "cartitem": cartitem}

            return render(request, 'orders/payement.html', context)

    context = {"orderform": orderform, "cartitem": cartitem}

    return render(request, 'orders/checkout.html', context)


def payement(request):

    return render(request, 'orders/payement.html')


def OrderServicess(request):

    profile = request.user

    cardtitem = CardItems.objects.filter(owner=profile)

    order_num = request.GET.get('ordernum')

    order = Order.objects.get(order_number=order_num,
                              owner=profile, is_ordered=False)

    for cartitem in cardtitem:

        orderproduct = OrderService.objects.create(

            order=order,

            owner=profile,

            service=cartitem.service,

            user=cartitem.service.owner,

            ordered=True)

        orderproduct.save()

    CardItems.objects.filter(owner=profile).delete()

    return redirect('index')
