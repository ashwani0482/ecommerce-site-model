from django.contrib import admin
from django.urls import path
from accounts.views import login_page, register_page, activate

urlpatterns = [
   path('login/',login_page, name= "login"),
   path('register/',register_page, name= "register"),
   path('activate/<email_token>/',activate, name= "activate"),

]