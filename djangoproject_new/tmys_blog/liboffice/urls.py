from django.urls import path


from . import views

urlpatterns = [
    path('', views.lib_index, name='lib_index'),
]