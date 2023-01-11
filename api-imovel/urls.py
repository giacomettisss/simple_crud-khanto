from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('all', views.getAllImovel),
    path('select/<pk>', views.getImovel),
    path('create', views.createImovel),
    path('update/<pk>', views.updateImovel),
    path('delete/<pk>', views.deleteImovel),
]
