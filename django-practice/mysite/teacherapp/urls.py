from django.urls import path
from . import views

app_name = 'teacherapp'

urlpatterns = [

    path('', views.index, name='index'),

]