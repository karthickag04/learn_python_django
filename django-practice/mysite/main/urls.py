from django.urls import path

from . import views


app_name = "main"


urlpatterns = [
    path("index/", views.index, name="index"),
     path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]