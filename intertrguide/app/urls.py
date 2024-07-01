from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aitg', views.aitg, name='aitg'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]