from django.db import models


class Hello(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Hi(models.Model):
    hello = models.ForeignKey(Hello, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
