from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/',views.about, name="about"),
    path('registration/', views.registration, name="registration"),
    path('adlogin/',views.adlogin, name="adlogin"),
    path('Login/',views.login, name="login"),
    path('logout/', views.logout, name='logout'), 
    path('organization/', views.organization, name="organization"),
    path('certification/', views.certification, name="certification"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('services/', views.services, name="services"),  
]