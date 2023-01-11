from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('all', views.getAllAnuncio),
    path('select/<pk>', views.getAnuncio),
    path('create', views.createAnuncio),
    path('update/<pk>', views.updateAnuncio),
]
