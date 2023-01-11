from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Anuncio
from .serializers import AnuncioSerializer
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Overview":"/",
        "Get all Anuncio":"/all",
        "Get one Anuncio":"/select/<pk>",
        "Create Anuncio":"/create",
        "Update Anuncio":"/update/<pk>",
    }
    return Response(api_urls)

@api_view(['GET'])
def getAllAnuncio(request):
    anuncio = Anuncio.objects.all()
    serializer = AnuncioSerializer(anuncio, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAnuncio(request, pk):
    anuncio = Anuncio.objects.get(id=pk)
    serializer = AnuncioSerializer(anuncio, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAnuncio(request):
    serializer = AnuncioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateAnuncio(request, pk):
    anuncio = Anuncio.objects.get(id=pk)
    serializer = AnuncioSerializer(instance=anuncio, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
