from django.db import models


class Move(models.Model):
    name = models.CharField(max_length=200)
    element = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    power = models.CharField(max_length=50)
    accuracy = models.CharField(max_length=50)
    pp = models.CharField(max_length=50)
    description = models.TextField()
    zmove = models.CharField(max_length=200)
    tm = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)