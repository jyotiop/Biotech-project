from django.urls import path
from . import views

app_name = 'studentapp'

urlpatterns = [
    path('', views.stuhome, name='stuhome'),
    path('stunews/', views.stunews, name='stunews'),
    path('stustudy/', views.stustudy, name='stustudy'),
    path('stufeedback/', views.stufeedback, name='stufeedback'),
    path('viewfeedback/', views.stuviewfeedback, name='stuviewfeedback'),
    
    
]
