from django.db import models


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.code

    class Meta:
        db_table = 'omnipro_store'
