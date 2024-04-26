from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("games", views.games, name="games"),
    path("background", views.background, name="background"),
    path("wiki", views.wiki, name="wiki"),
    path("mgr", views.mgr, name="mgr"),
    path("dmc", views.dmc, name="dmc"),
    path("mistral", views.mistral, name="mistral"),
    path("monsoon", views.monsoon, name="monsoon"),
    path("sundowner", views.sundowner, name="sundowner"),
    path("sam", views.sam, name="sam"),
    path("senator", views.senator, name="senator"),
    path("raiden", views.raiden, name="raiden"),
    path("dante", views.dante, name="dante"),
    path("vergil", views.vergil, name="vergil"),
]