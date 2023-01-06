from rest_framework import serializers
from .models import Client
from apps.country.serializers import CountrySerializer, StateSerializer, CitySerializer
from apps.store.serializers import StoreSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        """
        mediante este metodo se puede modificar la respuesta del serializer
        y se obtiene el objeto completo de los campos foraneos
        """
        self.fields['country_id'] = CountrySerializer(read_only=True)
        self.fields['state_id'] = StateSerializer(read_only=True)
        self.fields['city_id'] = CitySerializer(read_only=True)
        self.fields['favorite_store'] = StoreSerializer(read_only=True)
        return super(ClientSerializer, self).to_representation(instance)

    def validate(self, data):
        """
        antes de crear una cliente, se valida que el estado y la ciudad pertenezcan al pais,
        de lo contrario se lanza una excepcion.
        """
        if self.instance is None:
            if data['state_id'].country_id != data['country_id']:
                raise serializers.ValidationError('El estado no pertenece al pais')
            if data['city_id'].state_id != data['state_id']:
                raise serializers.ValidationError('La ciudad no pertenece al estado')
        return data
