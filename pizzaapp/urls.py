from django.contrib import admin
from django.urls import path
from .views import customerwelcomeview,userauthenticate,userloginview,signupuser,homepageview,adminloginview,adminhomepageview,authenticateadmin,logoutadmin,addpizza,deletepizza

urlpatterns = [
   path('admin/',adminloginview,name = 'adminloginpage'),
   path('adminauthenticate/',authenticateadmin),
   path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
   path('adminlogout/',logoutadmin),
   path('addpizza/',addpizza),
   path('deletepizza/<int:pizzak>/',deletepizza),
   path('',homepageview,name = 'homepage'),
   path('signupuser/',signupuser),
   path('loginuser/',userloginview,name = 'userloginpage'),
   path('customerwelcomeview/',customerwelcomeview,name = 'customerpage'),
   path('customer/authenticate/',userauthenticate)
]
