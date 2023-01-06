from django.db import models
from apps.country.models import Country, State, City
from apps.store.models import Store


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_id')
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_id')
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_id')
    favorite_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='favorite_store')

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.country_id.name + ' ' + \
            self.state_id.name + ' ' + self.city_id.name + ' ' + self.favorite_store.name

    class Meta:
        db_table = 'omnipro_client'
