from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('getnumber/', views.getnumber, name='getnumber'),
    path('result/back/', views.back, name='back')
]
