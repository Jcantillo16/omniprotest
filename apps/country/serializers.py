from rest_framework import serializers
from .models import Country, City, State


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        """
        aqui se valida la informacion antes de crear el objeto, que el pais no exista,
        y se genera el codigo del pais de manera automatica,
        el cual seran las 3 primeras letras del nombre del pais en mayusculas.
        """
        country = Country.objects.filter(name=validated_data['name'])
        if country:
            raise serializers.ValidationError("Country already exists")
        validated_data['code'] = validated_data['name'][:3].upper()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        metodo para actualizar la informacion de un pais, se valida que el nombre del pais no exista,
        y se actualiza el codigo del pais de manera automatica,
        el cual seran las 3 primeras letras del nombre del pais en mayusculas.
        """
        country = Country.objects.filter(name=validated_data['name'])
        if country:
            raise serializers.ValidationError("Country already exists")
        validated_data['code'] = validated_data['name'][:3].upper()
        return super().update(instance, validated_data)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'code']

    def to_representation(self, instance):
        """
        metodo para mostrar la informacion del estado, se agrega el nombre del pais al cual pertenece el estado.
        """
        data = super().to_representation(instance)
        data['country'] = CountrySerializer(instance.country_id).data
        return data

    def create(self, validated_data):
        """
        aqui se valida la informacion antes de crear el objeto, que el nombre del estado relacionado al pais no exista,
        y se genera el codigo del estado de manera automatica,
        """
        state = State.objects.filter(
            name=validated_data['name'],
            country_id=validated_data['country_id'])

        if state:
            raise serializers.ValidationError("State already exists")

        validated_data['code'] = validated_data['name'][:3].upper()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        metodo para actualizar la informacion de un estado, se valida que el nombre del estado relacionado al pais no exista,
        y se actualiza el codigo del estado de manera automatica,
        """
        country_id = validated_data.get(
            'country_id',
            instance.country_id)

        state = State.objects.filter(
            name=validated_data['name'],
            country_id=country_id)

        if state:
            raise serializers.ValidationError("State already exists")

        validated_data['code'] = validated_data['name'][:3].upper()
        return super().update(instance, validated_data)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'code']


    def to_representation(self, instance):
        """
        metodo para mostrar la informacion de la ciudad, se agrega el nombre del estado al cual pertenece la ciudad.
        """
        data = super().to_representation(instance)
        data['state_and_country'] = StateSerializer(instance.state_id).data
        return data

    def create(self, validated_data):
        """
        aqui se valida la informacion antes de crear el objeto, que el nombre de la ciudad relacionado al estado no exista,
        y se genera el codigo de la ciudad de manera automatica,
        """
        city = City.objects.filter(
            name=validated_data['name'],
            state_id=validated_data['state_id'])

        if city:
            raise serializers.ValidationError("City already exists")

        validated_data['code'] = validated_data['name'][:3].upper()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        metodo para actualizar la informacion de una ciudad, se valida que el nombre de la ciudad relacionado al estado no exista,
        y se actualiza el codigo de la ciudad de manera automatica,
        """
        state_id = validated_data.get(
            'state_id',
            instance.state_id)

        city = City.objects.filter(
            name=validated_data['name'],
            state_id=state_id)

        if city:
            raise serializers.ValidationError("City already exists")

        validated_data['code'] = validated_data['name'][:3].upper()
        return super().update(instance, validated_data)

