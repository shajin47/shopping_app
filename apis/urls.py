from django.urls import path
from .views import register, getUser

urlpatterns = [
    path("register/",register, name="register"),
    path("getUsers/",getUser, name="getUsers")
]
