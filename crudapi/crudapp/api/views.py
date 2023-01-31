from rest_framework.response import Response
from rest_framework.decorators import api_view
from crudapp.models import Animal_info
from crudapp.api.serializers import Animal_infoSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def get_list(request):
    if request.method == 'GET':
        Animal_list = Animal_info.objects.all()
        serializer = Animal_infoSerializer(Animal_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Animal_infoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST', 'DELETE'])
def get_details(request, pk):
    if request.method == "GET":
        try:
            Animal_list = Animal_info.objects.get(pk=pk)
        except Animal_info.DoesNotExist:
            return Response({'Error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = Animal_infoSerializer(Animal_list)
        return Response(serializer.data)

    if request.method == "PUT":
        Animal_list = Animal_info.objects.get(pk=pk)
        serializer = Animal_infoSerializer(Animal_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Animal_list = Animal_info.objects.get(pk=pk)
        Animal_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)