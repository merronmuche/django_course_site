from django.urls import path
from . import views


urlpatterns = [
    path('new/', views.index),
    path('base/', views.base),
]