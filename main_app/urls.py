from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # subsequent paths go here, no longer need to go to catcollector/urls.py
    path('about/', views.about, name='about')
]
