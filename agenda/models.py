from django.db import models


class Agenda(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=25)
    favourite = models.BooleanField()

    def __str__(self):
        return self.name
