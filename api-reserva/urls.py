from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview),
    path('all', views.getAllReserva),
    path('select/<pk>', views.getReserva),
    path('create', views.createReserva),
    path('delete/<pk>', views.deleteReserva),
]
