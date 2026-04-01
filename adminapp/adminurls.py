from django.urls import path
from .import views



urlpatterns =[
    path('', views.adparent, name="adparent"),
    path('adnews/',views.adnews,name="adnews"),
    path('adhome/',views.adhome,name="adhome"),
    path('adbranch/',views.adbranch,name="adbranch"),
    path('adcourse/', views.adcourse, name="adcourse"),
    path('adsession/',views.adsession,name="adsession"),
    path('adstudy/', views.adstudy, name="adstudy"),
    path('adstudent/', views.adstudent, name="adstudent"),
    path('viewstudy/', views.viewstudy, name="viewstudy"),
    path('editbranch/<id>',views.editbranch,name="editbranch"),
    path('deletebranch/<id>',views.deletebranch,name="deletebranch"),
    path('editcourse/<id>',views.editcourse,name="editcourse"),
    path('deletecourse/<id>',views.deletecourse,name="deletecourse"),
    path('editsession/<id>',views.editsession,name="editsession"),
    path('deletesession/<id>',views.deletesession,name="deletesession"),
    path('adstudy/', views.adstudy,name="adstudy"),
    path('editstudy/<id>',views.editstudy,name="editstudy"),
    path('deletestudy/<id>',views.deletestudy,name="deletestudy"),

]
