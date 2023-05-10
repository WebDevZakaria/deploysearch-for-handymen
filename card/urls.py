from django.urls import path
from . import views


urlpatterns = [

    path('addtocard/<str:pk>', views.addtocard, name='add-to'),

    path('', views.card, name='cart'),
    path('removeitem/<str:pk>', views.cardremove, name='remove-item'),

]
