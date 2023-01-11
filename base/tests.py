from rest_framework import status
from rest_framework.test import APITestCase
from .models import Imovel, Anuncio, Reserva
from rest_framework.utils.serializer_helpers import ReturnList


class ApiTestCase(APITestCase):

    @classmethod
    def setUp(cls):
        Imovel(guest_limit=4, bathrooms=2, accept_pet=True, cleaning_price=70, activated_at='2022-01-01').save()
        Anuncio(id_imovel=Imovel.objects.get(id=1), plataform_name='Airbnb', plataform_tax=39.99).save()
        Reserva(id_anuncio=Anuncio.objects.get(id=1), chekin_at='2022-01-03', checkout_at='2022-01-10', total_price=399.98, guest_amount=2).save()


    # IMOVEL
    def test_imovel_base(self):
        response = self.client.get('/imovel/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_imovel_all(self):
        response = self.client.get('/imovel/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), ReturnList)


    def test_imovel_select(self):
        response = self.client.get('/imovel/select/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_imovel_create(self):
        data = dict(
            guest_limit=4,
            bathrooms=2,
            accept_pet=False,
            cleaning_price=50,
            activated_at='2022-01-01'
        )
        response = self.client.post('/imovel/create', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['guest_limit'], response.data['guest_limit'])
        self.assertEqual(data['bathrooms'], response.data['bathrooms'])
        self.assertEqual(data['accept_pet'], response.data['accept_pet'])
        self.assertEqual(data['activated_at'], response.data['activated_at'])


    def test_imovel_update(self):
        data = dict(
            guest_limit=4,
            bathrooms=2,
            accept_pet=False,
            cleaning_price=50,
            activated_at='2022-01-01'
        )
        response = self.client.post('/imovel/update/1', data=data)
        self.assertEqual(data['guest_limit'], response.data['guest_limit'])
        self.assertEqual(data['bathrooms'], response.data['bathrooms'])
        self.assertEqual(data['accept_pet'], response.data['accept_pet'])
        self.assertEqual(data['activated_at'], response.data['activated_at'])


    def test_imovel_delete(self):
        response = self.client.delete('/imovel/delete/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # ANUNCIO
    def test_anuncio_base(self):
        response = self.client.get('/anuncio/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_anuncio_all(self):
        response = self.client.get('/anuncio/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), ReturnList)


    def test_anuncio_select(self):
        response = self.client.get('/anuncio/select/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_imovel_create(self):
        data = dict(
            id_imovel=1,
            plataform_name='booking.com',
            plataform_tax='49.99'
        )
        response = self.client.post('/anuncio/create', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['id_imovel'], response.data['id_imovel'])
        self.assertEqual(data['plataform_name'], response.data['plataform_name'])
        self.assertEqual(data['plataform_tax'], response.data['plataform_tax'])


    def test_imovel_update(self):
        data = dict(
            id_imovel=1,
            plataform_name='booking.com',
            plataform_tax='49.99'
        )
        response = self.client.post('/anuncio/update/1', data=data)
        self.assertEqual(data['id_imovel'], response.data['id_imovel'])
        self.assertEqual(data['plataform_name'], response.data['plataform_name'])
        self.assertEqual(data['plataform_tax'], response.data['plataform_tax'])


    # RESREVA
    def test_reserva_select(self):
        response = self.client.get('/reserva')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_reserva_select(self):
        reserva_1 = Reserva.objects.get(id_anuncio=1)
        response = self.client.get(f'/reserva/select/{str(reserva_1.id)}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_reserva_all(self):
        response = self.client.get('/reserva/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.data), ReturnList)


    def test_reserva_create(self):
        data = dict(
            id_anuncio=1,
            chekin_at='2022-01-14',
            checkout_at='2022-01-21',
            total_price='499.99',
            comment="Imóvel e lugar lindo!",
            guest_amount=2
        )
        response = self.client.post('/reserva/create', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['id_anuncio'], response.data['id_anuncio'])
        self.assertEqual(data['chekin_at'], response.data['chekin_at'])
        self.assertEqual(data['checkout_at'], response.data['checkout_at'])
        self.assertEqual(data['total_price'], response.data['total_price'])
        self.assertEqual(data['comment'], response.data['comment'])
        self.assertEqual(data['guest_amount'], response.data['guest_amount'])