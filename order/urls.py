from django.urls import path

from order import views


urlpatterns = [

    path('', views.checkoute, name="checkout"),

    path('payement/', views.payement, name='payement'),

    path('sucess/', views.OrderServicess, name='order-success'),


]
