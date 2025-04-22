from django.urls import path
from .import views


urlpatterns = [
    path('', views.mydream),
    path('mydream', views.mydream)
]

