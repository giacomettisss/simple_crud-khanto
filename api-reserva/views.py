from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Reserva
from .serializers import ReservaSerializer
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Overview":"/",
        "Get all Reserva":"/all",
        "Get one Reserva":"/select/<pk>",
        "Create Reserva":"/create",
        "Delete Reserva":"/delete/<pk>",
    }
    return Response(api_urls)

@api_view(['GET'])
def getAllReserva(request):
    reserva = Reserva.objects.all()
    serializer = ReservaSerializer(reserva, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    serializer = ReservaSerializer(reserva, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createReserva(request):
    serializer = ReservaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def deleteReserva(request, pk):
    reserva = Reserva.objects.get(id=pk)
    reserva.delete()
    return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)
