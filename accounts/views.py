from email.message import EmailMessage
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import Account
from .forms import Registerform
from django.contrib import messages, auth
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import force_bytes

from django.contrib.auth.tokens import default_token_generator

from django.core.mail import EmailMessage

from service.models import Createservice

from .models import Account, Message

from service.models import Service

from order.models import OrderService
from.forms import formmessage


def registers(request):

    if request.method == 'POST':

        register = Registerform(request.POST, request.FILES)

        if register.is_valid():

            first_name = register.cleaned_data['first_name']
            last_name = register.cleaned_data['last_name']
            phone_number = register.cleaned_data['phone_number']
            email = register.cleaned_data['email']
            wilaya = register.cleaned_data['wilaya']
            profile_image = register.cleaned_data['profile_image']
            is_servicecreator = register.cleaned_data['is_servicecreator']
            password = register.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(

                first_name=first_name, last_name=last_name, email=email, username=username, password=password)

            user.phone_number = phone_number
            user.is_servicecreator = is_servicecreator
            user.wilaya = wilaya
            user.profile_image = profile_image

            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('active_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            return redirect('/account/login/?command=verification&email='+email)

    register = Registerform()

    context = {'reg': register}

    return render(request, 'users/register.html', context)


def activatee(request, uidb64, token):

    uid = urlsafe_base64_decode(uidb64).decode()

    user = Account._default_manager.get(pk=uid)

    if user is not None and default_token_generator.check_token(user, token):

        user.is_active = True
        user.save()
        messages.success(
            request, 'your account is activated avec successs ! thnx')

        return redirect('index')

    else:
        messages.error(request, 'invalid link ')

        return redirect('register-home')


def logine(request):

    if request.method == 'POST':

        email = request.POST['email']

        password = request.POST['password']

        user = Account.objects.get(email=email)

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active:

            login(request, user)

            return redirect("index")
        else:
            print('somethine wrong')

            messages.error(

                request, ' enable thomething went wrong ')

    return render(request, 'users/login.html')


def logoute(request):

    logout(request)

    return redirect('index')


def Adminpage(request):

    service = Createservice.objects.all()

    message = Message.objects.filter(recipient=request.user)

    context = {"service": service, "message": message}

    return render(request, 'users/admin.html', context)


def ShowUsers(request):

    account = Account.objects.all()

    context = {"account": account}

    return render(request, 'users/all_users.html', context)


def ShowService(request):

    profile = request.user

    service = Service.objects.all()

    context = {"service": service}

    return render(request, 'users/yourservice.html', context)


def AccepteService(request, pk):
    service = Createservice.objects.get(id=pk)

    servicess = Service.objects.create(

        owner=service.user,
        Service_name=service.Service_name,
        description=service.description,
        image=service.images,
        category=service.category,
        wilaya=service.user.wilaya,
        baladiya=service.baladiya

    )

    servicess.save()
    service.delete()

    return redirect('admin-page')


def DeleteService(request, pk):

    servicesss = Createservice.objects.get(id=pk)
    servicesss.delete()
    return redirect('admin-page')


def DeleteServices(request, pk):
    servicese = Service.objects.get(id=pk)
    servicese.delete()
    return redirect('your-service')


def ServiceCommande(request):

    order = OrderService.objects.filter(user=request.user)

    context = {"service": order}

    return render(request, 'users/servicecommande.html', context)


def orderedCommande(request, pk):

    ordered = OrderService.objects.get(id=pk)

    ordered.delete()

    return redirect('service-commande')


def AdminProfiles(request):

    profile = Account.objects.filter(is_admin=True)

    context = {"profile": profile}

    return render(request, 'users/adminprofiles.html', context)


def userprofiless(request, pk):

    profiles = Account.objects.get(id=pk)

    context = {"profile": profiles}

    return render(request, 'users/userprofiles.html', context)


def sendmessage(request, pk):

    profile = Account.objects.get(id=pk)

    form = formmessage()

    if request.method == "POST":
        form = formmessage(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.sender = request.user
            forms.recipient = profile
            forms.save()
            return redirect("user-pro", pk)

    context = {"form": form}

    return render(request, 'users/sendmessage.html', context)


def dashboard(request):

    orders = OrderService.objects.filter(owner=request.user)

    ordd = orders.count()

    profile = Account.objects.get(id=request.user.id)

    context = {"ordd": ordd, "orders": orders, "profile": profile}

    return render(request, 'users/dashboard.html', context)


def myorder(request):

    orderss = OrderService.objects.filter(owner=request.user)

    context = {"order": orderss}

    return render(request, 'users/myorders.html', context)


def MessageContent(request, pk):

    messag = Message.objects.get(id=pk)

    messag.is_read = True

    messag.save()

    message = Message.objects.filter(recipient=request.user)

    context = {"messag": messag, "message": message}

    return render(request, 'users/messagecontent.html', context)
