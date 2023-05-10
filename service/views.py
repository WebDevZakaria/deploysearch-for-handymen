from django.shortcuts import render, redirect


# Create your views here.

from .models import Service, Category, Wilaya, Createservice, baladiya
from .forms import Serviceform
from service import forms

from django.contrib.auth.decorators import login_required

from order.models import OrderService
from .models import ReviewRating
from.forms import reviews


def index(request):

    service = Service.objects.all()

    context = {'service': service}

    return render(request, 'services/index.html', context)


def categoryservice(request, pk):

    wilaya = Wilaya.objects.get(id=pk)

    #category = Category.objects.filter(wilaya=wilaya)
    balad = baladiya.objects.filter(wilaya=wilaya)

    service = Service.objects.filter(wilaya=wilaya)

    context = {"baladiya": balad, "service": service, "wilaya": wilaya}

    return render(request, 'services/categoryall.html', context)


def categoryDetail(request, pk):

    #category = Category.objects.get(id=pk)
    
    balad = baladiya.objects.get(id=pk)
    
    category = Category.objects.filter(baladiya=balad)

    service = Service.objects.filter(baladiya=balad)

    counter = service.count()

    context = {"service": service, "counter": counter, "category": category}

    return render(request, 'services/categoryproduct.html', context)


def categoryfinal(request, pk):

    category = Category.objects.get(id=pk)

    service = Service.objects.filter(category=category)

    context = {"service": service}

    return render(request, 'services/categoryfinal.html', context)


@login_required
def createservice(request):

    if request.method == 'POST':

        user = request.user

        services = Serviceform(request.POST, request.FILES, user=user)

        if services.is_valid():

            servicess = services.save(commit=False)

            servicess.user = user

            servicess.save()

            return redirect('index')

    else:

        user = request.user

        services = Serviceform(user=user)

    context = {"service": services}

    return render(request, 'services/createservice.html', context)


def load_cities(request):

    baladiya_id = request.GET.get('baladiya_id')

    cities = Category.objects.filter(baladiya_id=baladiya_id).all()

    return render(request, 'services/city_dropdown_list_options.html', {'cities': cities})


def serviceDetail(request, pk):
    service = Service.objects.get(id=pk)

    if request.user.is_authenticated:

        orderproduct = OrderService.objects.filter(
            owner=request.user, service=service).exists()

    else:

        orderproduct = None

    #show = service.reviewrating_set.all()
    show = ReviewRating.objects.filter(service=service)

    Avg = 0
    total = 0
    count = 0

    reviewaverage = ReviewRating.objects.filter(service=service)
    for average in reviewaverage:
        total += average.rating
        count += 1
    if reviewaverage:
        Avg = total/count

    context = {"service": service, "show": show,
               "orderproduct": orderproduct, "Avg": Avg}

    return render(request, 'services/servicesdetail.html', context)


def submit_review(request, service_id):

    url = request.META.get('HTTP_REFERER')

    if request.method == "POST":

        try:
            reviewss = ReviewRating.objects.get(
                owner=request.user, service__id=service_id)

            forms = reviews(request.POST, instance=reviewss)

            forms.save()

            return redirect(url)

        except ReviewRating.DoesNotExist:

            forms = reviews(request.POST)

            if forms.is_valid():

                formss = forms.save(commit=False)

                formss.owner = request.user

                formss.service_id = service_id

                formss.ip = request.META.get('REMOTE_ADDR')

                formss.save()

                return redirect(url)
