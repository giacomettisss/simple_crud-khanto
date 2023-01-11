from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Imovel
from .serializers import ImovelSerializer
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Overview":"/",
        "Get all Imovel":"/all",
        "Get one Imovel":"/select/<pk>",
        "Create Imovel":"/create",
        "Update Imovel":"/update/<pk>",
        "Delete Imovel":"/delete/<pk>",
    }
    return Response(api_urls)

@api_view(['GET'])
def getAllImovel(request):
    imovel = Imovel.objects.all()
    serializer = ImovelSerializer(imovel, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getImovel(request, pk):
    imovel = Imovel.objects.get(id=pk)
    serializer = ImovelSerializer(imovel, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createImovel(request):
    serializer = ImovelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateImovel(request, pk):
    imovel = Imovel.objects.get(id=pk)
    serializer = ImovelSerializer(instance=imovel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def deleteImovel(request, pk):
    imovel = Imovel.objects.get(id=pk)
    imovel.delete()
    return Response('Successfully deleted', status=status.HTTP_204_NO_CONTENT)