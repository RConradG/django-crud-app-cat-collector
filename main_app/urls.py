from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # subsequent paths go here, no longer need to go to catcollector/urls.py
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
]
