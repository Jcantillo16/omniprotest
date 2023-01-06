import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.country.models import Country, State, City
from apps.store.models import Store
from apps.client.models import Client
from data import STATES, COUNTRIES, CITIES, STORES

import random

#validar conexion a la base de datos



def validate_country(country):
    """
    aqui se valida que el pais no exista
    """
    country = Country.objects.filter(name=country)
    if country:
        return True
    return False



def validate_store(store):
    """
    aqui se valida que la tienda no exista
    """
    store = Store.objects.filter(name=store).first()
    if store:
        return True
    return False


def validate_state(state):
    """
    aqui se valida que el estado no exista
    """
    state = State.objects.filter(name=state).first()
    if state:
        return True
    return False


def validate_city(city):
    """
    aqui se valida que la ciudad no exista
    """
    city = City.objects.filter(name=city).first()
    if city:
        return True
    return False


def create_country():
    """
    mediante este método se crean los países, se toma como datos semilla
    la lista COUNTRIES, la cual contiene los nombres de los países,
    se llama dentro de este metodo a validate_country, el cual valida que el pais no exista
    """
    try:
        for country in COUNTRIES:
            if not validate_country(country):
                Country.objects.create(name=country, code=country[:3].upper())
                print(f'Country {country} created')
            else:
                print(f'Country {country} already exists')
    except Exception as e:
        print(e)


def create_state():
    """
    mediante este método se crean los estados, se toma como datos semilla
    la lista STATES, la cual contiene los nombres de los estados,
    se llama dentro de este metodo a validate_state, el cual valida que el estado no exista
    """
    try:
        for state in STATES:
            for country, states in state.items():
                for state in states:
                    if not validate_state(state):
                        State.objects.create(name=state, country_id=Country.objects.get(name=country),
                                             code=state[:3].upper())
                        print(f'State {state} created')
                    else:
                        print(f'State {state} already exists')
    except Exception as e:
        print(e)


def create_city():
    """
    mediante este método se crean las ciudades, se toma como datos semilla
    la lista CITIES, la cual contiene los nombres de las ciudades,
    se llama dentro de este metodo a validate_city, el cual valida que la ciudad no exista
    """
    try:
        for city in CITIES:
            for state, cities in city.items():
                for city in cities:
                    if not validate_city(city):
                        City.objects.create(name=city, state_id=State.objects.get(name=state), code=city[:3].upper())
                        print(f'City {city} created')
                    else:
                        print(f'City {city} already exists')
    except Exception as e:
        print(e)


def create_store():
    """
    mediante este método se crean las tiendas, se toma como datos semilla
    la lista STORES, la cual contiene los nombres de las tiendas,
    se llama dentro de este metodo a validate_store, el cual valida que la tienda no exista
    """
    try:
        for store in STORES:
            if not validate_store(store):
                Store.objects.create(name=store)
                print(f'Store {store} created')
            else:
                print(f'Store {store} already exists')
    except Exception as e:
        print(e)


def create_client():
    """
    mediante este método se crearan 10 clientes,
    a cada cliente se le asignara un pais (id) diferente,
    el estado(id) y la ciudad(id) que se le asignen deben pertenecer al pais que se le asigno,
    a cada cliente se le asignara una tienda favorita
    """
    try:
        for i in range(1, 11):
            country = Country.objects.get(id=random.randint(1, 5))
            state = State.objects.filter(country_id=country).first()
            city = City.objects.filter(state_id=state).first()
            store = Store.objects.get(id=random.randint(1, 5))
            Client.objects.create(
                name=f'client{i}',
                surname=f'surname{i}',
                country_id=country,
                state_id=state,
                city_id=city,
                favorite_store=store)
            print(f'Client {i} created')

    except Exception as e:
        print(e)


def update_client():
    for i in [5, 8, 9]:
        try:
            client = Client.objects.get(id=i)
            client.name = 'Julián'
            client.save()
            print(f'Client with id {i} updated')
        except Exception as e:
            print(e)


def update_client_store():
    """
    Los clientes con id 1,7,6 debe tener la tienda con el id 5 como tienda favorita
    """
    for i in [1, 7, 6]:
        try:
            client = Client.objects.get(id=i)
            client.favorite_store = Store.objects.get(id=5)
            client.save()
            print(f'Client with id {i} updated, new favorite store ')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    create_country()
    create_state()
    create_city()
    create_store()
    create_client()
    update_client()
    update_client_store()
