from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
     path("user/login/", views.login, name="lin"),
    path("user/signup/", views.signup, name="sup"),
    path("profile/disable", views.disable, name="disable"),
    path("logout/", views.user_logout, name="logout")
]
