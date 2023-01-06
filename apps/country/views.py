from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer
from django.http import Http404

"""
    CountryView: clase para listar todos los paises, crear un nuevo pais, y eliminar todos los paises.
    CountryDetailView: clase para obtener, actualizar y eliminar un pais.
    StateView: clase para listar todos los estados, crear un nuevo estado, y eliminar todos los estados.
    StateDetailView: clase para obtener, actualizar y eliminar un estado.
    CityView: clase para listar todos las ciudades, crear una nueva ciudad, y eliminar todas las ciudades.
    CityDetailView: clase para obtener, actualizar y eliminar una ciudad.
    
    Para cada clase se implementa el metodo get, post, put, delete, y el metodo get_object.
    get: metodo para obtener la informacion de un objeto.
    post: metodo para crear un nuevo objeto.
    put: metodo para actualizar la informacion de un objeto.
    delete: metodo para eliminar un objeto.
    get_object: metodo para obtener un objeto.
    
"""


class CountryView(APIView):
    def get(self, request):
        """
        mediante este metodo se obtiene la lista de paises
        en la resuesta se envia un json con la lista de paises y la cantidad de registros
        """
        countries = Country.objects.all()
        data = CountrySerializer(countries, many=True).data
        count = countries.count()
        return Response({'count': count, 'results': data})

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetailView(APIView):
    def get_object(self, pk):
        """
        metodo para obtener un pais por su id
        """
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        mediante este metodo se obtiene la informacion de un pais, mediante su id
        """
        country = self.get_object(pk)
        data = CountrySerializer(country).data
        return Response(data)

    def put(self, request, pk):
        """
        mediante este metodo se actualiza la informacion de un pais, mediante su id,
        al actualizar la informacion se valida que el nombre del pais no exista,
        y se actualiza el codigo del pais de manera automatica, haciendo uso del serializer.
        """
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        mediante este metodo se elimina un pais, mediante su id
        """
        try:
            country = self.get_object(pk)
            country.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
aqui se crean las vistas para los estados, se hace uso de los metodos get, post, put y delete
para obtener la lista de estados, crear un estado, actualizar un estado y eliminar un estado
"""


class StateView(APIView):
    def get(self, request):
        states = State.objects.all()
        data = StateSerializer(states, many=True).data
        return Response(data)

    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateDetailView(APIView):
    def get_object(self, pk):
        try:
            return State.objects.get(pk=pk)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        state = self.get_object(pk)
        data = StateSerializer(state).data
        return Response(data)

    def put(self, request, pk):
        state = self.get_object(pk)
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            state = self.get_object(pk)
            state.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""
Aqui los metodos correspondientes para las ciudades, (get, post, put, delete)
las validaciones de los metodos son llamadas desde el serializer.
"""


class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        data = CitySerializer(cities, many=True).data
        count = cities.count()
        return Response({
            'count': count,
            'results': data})

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailView(APIView):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        city = self.get_object(pk)
        data = CitySerializer(city).data
        return Response(data)

    def put(self, request, pk):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            city = self.get_object(pk)
            city.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
