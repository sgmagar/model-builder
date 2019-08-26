from django.db import models


class SecondHello(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=20, blank=True)
    age = models.PositiveSmallIntegerField()


class SecondHi(models.Model):
    hello = models.ForeignKey(SecondHello, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
