from rest_framework import serializers
from .models import Store
import random


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        """
        valida que la tienda no exista
        mediante este metodo se genera un codigo de 6 digitos para la tienda,
        el cual son las primeras 3 letras del nombre de la tienda (mayusculas) mas 3 digitos aleatorios
        """
        if Store.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('the store already exists')
        code = validated_data['name'][:3].upper() + str(random.randint(100, 999))
        validated_data['code'] = code
        return super(StoreSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """
        mediante este metodo se actualiza la informaion de la tienda,
        se genera un nuevo codigo si se cambia el nombre.
        """
        if instance.name != validated_data['name']:
            code = validated_data['name'][:3].upper() + str(random.randint(100, 999))
            validated_data['code'] = code
        return super(StoreSerializer, self).update(instance, validated_data)
