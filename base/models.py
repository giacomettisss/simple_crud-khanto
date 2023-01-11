import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your models here.

class Imovel(models.Model):
    guest_limit = models.IntegerField()
    bathrooms = models.IntegerField()
    accept_pet = models.BooleanField()
    cleaning_price = models.DecimalField(max_digits=19, decimal_places=2)
    activated_at =  models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Anuncio(models.Model):
    id_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataform_name = models.CharField(max_length=512)
    plataform_tax = models.DecimalField(max_digits=19, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reserva(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    chekin_at = models.DateField()
    checkout_at = models.DateField()
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    comment = models.TextField(max_length=2048, blank=True)
    guest_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)