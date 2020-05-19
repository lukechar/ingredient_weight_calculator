from django.urls import path

from . import views

urlpatterns = [
    path('', views.calculator_form, name='calculator_form'),
    path('do_calc/', views.calculate, name='calculate'),
]