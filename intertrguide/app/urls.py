from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('aitg', views.aitg, name='aitg'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout/', logout_view, name='logout'),
]