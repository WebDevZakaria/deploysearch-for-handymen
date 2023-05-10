from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('category/<str:pk>', views.categoryservice, name='category'),

    path('categorydetail/<str:pk>', views.categoryDetail, name='categorydetail'),
    path('categoryfinal/<str:pk>', views.categoryfinal, name='categoryfinal'),

    path('createservice', views.createservice, name='create-service'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),


    path('servicedetail/<str:pk>', views.serviceDetail, name='show-detail'),

    path('submitreview/<str:service_id>',
         views.submit_review, name="submit-review"),
]
