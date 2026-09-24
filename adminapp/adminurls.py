from django.urls import path
from . import views

urlpatterns = [
    path('', views.adparent, name="adparent"),
    path('adhome/', views.adhome, name="adhome"),
    path('adnews/', views.adnews, name="adnews"),
    path('editnews/<int:id>/', views.editnews, name="editnews"),
    path('deletenews/<int:id>/', views.deletenews, name="deletenews"),
    path('adbranch/', views.adbranch, name="adbranch"),
    path('editbranch/<int:id>/', views.editbranch, name="editbranch"),
    path('deletebranch/<int:id>/', views.deletebranch, name="deletebranch"),
    path('adcourse/', views.adcourse, name="adcourse"),
    path('editcourse/<int:id>/', views.editcourse, name="editcourse"),
    path('deletecourse/<int:id>/', views.deletecourse, name="deletecourse"),
    path('adsession/', views.adsession, name="adsession"),
    path('editsession/<int:id>/', views.editsession, name="editsession"),
    path('deletesession/<int:id>/', views.deletesession, name="deletesession"),
    path('adstudent/', views.adstudent, name="adstudent"),
    path('adstudy/', views.adstudy, name="adstudy"),
    path('viewstudy/', views.viewstudy, name="viewstudy"),
    path('editstudy/<int:id>/', views.editstudy, name="editstudy"),
    path('deletestudy/<int:id>/', views.deletestudy, name="deletestudy"),
    path('viewenquiries/', views.viewenquiries, name="viewenquiries"),
    path('deleteenquiry/<int:id>/', views.deleteenquiry, name="deleteenquiry"),
]
