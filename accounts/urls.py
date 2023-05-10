from django.urls import path
from . import views


urlpatterns = [




    path('register/', views.registers, name='register-home'),
    path('activate/<uidb64>/<token>/', views.activatee, name="activate"),
    path('logout/', views.logoute, name='logout'),
    path('login/', views.logine, name='login'),
    path('adminpage/', views.Adminpage, name='admin-page'),
    path('showuser/', views.ShowUsers, name='all-users'),
    path('showservice/', views.ShowService, name='your-service'),
    path('accepteservice/<str:pk>', views.AccepteService, name='accepte-service'),
    path('deleteservice/<str:pk>', views.DeleteService, name='delete-sevice'),
    path('deleteservices/<str:pk>', views.DeleteServices, name='delete-services'),
    path('commandepage/', views.ServiceCommande, name='service-commande'),
    path('orderedservice/<str:pk>', views.orderedCommande, name='ordered-service'),
    path('adminprofiles/', views.AdminProfiles, name='profiles'),
    path('userprofile/<str:pk>', views.userprofiless, name='user-pro'),
    path('sendmessage/<str:pk>', views.sendmessage, name='send-message'),

    path('dashboard/', views.dashboard, name="dash-board"),
    path('myorders/', views.myorder, name="my-orders"),
    #path('editprofile/', views.editprofile, name="edit-profile"),

    path('messagecontent/<str:pk>', views.MessageContent, name="message-content"),




]
