from django.urls import path, include
from . import views

urlpatterns = [
    path('index.html', views.index),
    path('contact', views.contact, name='contact_create'),
    path('see', views.see, name='see'),
]
