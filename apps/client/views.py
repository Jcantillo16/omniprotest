from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from django.http import Http404


class ClientList(APIView):
    def get(self, request):
        """
        se obtienen todos los clientes
        """
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        count = clients.count()
        return Response({'count': count, 'clients': serializer.data})

    def post(self, request):
        """
        se crea un cliente
        """
        try:
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    def get_object(self, pk):
        """
        se obtiene un cliente por su id
        """
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        se obtiene un cliente por su id
        """
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def patch(self, request, pk):
        """
        se actualiza un cliente por su id, utilice este metodo para actualizar solo algunos campos
        """
        try:
            client = self.get_object(pk)
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error ': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        se elimina un cliente por su id
        """
        try:
            client = self.get_object(pk)
            client.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error ': str(e)}, status=status.HTTP_400_BAD_REQUEST)
