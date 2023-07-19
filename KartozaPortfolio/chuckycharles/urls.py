from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("index/", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profileuser, name="profile"),
    path("allusers", views.allusers, name="profile"),
]