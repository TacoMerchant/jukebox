# added from polls tutorial
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]