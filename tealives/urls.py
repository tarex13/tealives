from django.contrib import admin
from django.urls import path, include
from accounts.views import login, user_logout
from . import views
urlpatterns = [
    path("", login, name="lin"),
    path("logout/", user_logout),
    path("reset/", views.fp, name="resetpass"),
    path("events/", views.events, name="events"),
    path("accounts/user/login/", views.lin2, name="lin2"),
path("accounts/user/resetpass/", views.fp, name="fp"),
path("accounts/profile/edit/", views.edit, name="editAccount"),
path("accounts/profile/pass/change/", views.changePass, name="changePass"),
path("accounts/profile/security/", views.accountsec, name="accountsec"),
path("accounts/profile/preferences/", views.pref, name="pref"),
path("accounts/activity/", views.acc_activity, name="acc_activity"),
path("NotFound/", views.settings, name="settings"),
path("chat/dm/", views.dm, name="dm"),
path("chat/room/<str:chat_room>", views.dm_room, name="dm_room"),
path("create/", views.create, name="create"),
path("<str:username>/", views.profile, name="prof"),
path("<str:username>/about/", views.aboutPage, name="aboutPage"),
]
