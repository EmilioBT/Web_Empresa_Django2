from django.urls import path
from . import views

urlpatterns = [
    # Path de services
    path('', views.services, name='services'),

]