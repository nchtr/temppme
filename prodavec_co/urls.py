from django.urls import path
from prodavec_co import views


urlpatterns = [
    path('', views.index, name='index'),
]
