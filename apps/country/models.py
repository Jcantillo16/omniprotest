from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.name + ' ' + self.code

    class Meta:
        db_table = 'omnipro_country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']


class State(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True, default=None)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')

    def __str__(self):
        return self.name + ' ' + self.code

    class Meta:
        db_table = 'omnipro_state'


class City(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True, default=None)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.code

    class Meta:
        db_table = 'omnipro_city'
