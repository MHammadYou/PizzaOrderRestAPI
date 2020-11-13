from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    price = models.FloatField()
    pieces = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
