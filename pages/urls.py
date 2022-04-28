from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('terms_and_conditions', views.terms_and_conditions,
         name='terms_and_conditions')
]
