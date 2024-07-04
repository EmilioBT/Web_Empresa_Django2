from django.urls import path
from . import views

urlpatterns = [
    # Path de contact
    path('', views.contact, name='contact'),
]