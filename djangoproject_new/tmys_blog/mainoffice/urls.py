from django.urls import path
from . import views


urlpatterns = [

path("", views.home, name="home"),
path("services", views.services1, name="services"),

]