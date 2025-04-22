from django.urls import path
from . import views



urlpatterns = [
    path('', views.myworklife),
    path('myworklife', views.myworklife),
    path('mycv', views.mycv),
    path('Dataanalyst', views.Dataanalyst)
]
