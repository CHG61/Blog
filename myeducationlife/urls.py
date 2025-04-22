from . import views
from django.urls import path



urlpatterns = [
    path('', views.myeducationlife),
    path('myeducationlife', views.myeducationlife),
    path('erasmus', views.erasmus),
    path('university', views.university),
    path('data', views.data),
    path('sports', views.sports),
]
