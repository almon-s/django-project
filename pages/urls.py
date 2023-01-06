"""Defines URL patterns for pages."""

from django.urls import path

from . import views

app_name = "pages"
urlpatterns = [
    path("", views.home, name="home"),
    path("page1/", views.page1, name="page1"),
    path("htmlpage/", views.google, name="google"),
] 