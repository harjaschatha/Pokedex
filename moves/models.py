from django.db import models
import re


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
    slug = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{}'.format(self.name)

    def generate_slug(self, s):
        #https://blog.dolphm.com/slugify-a-string-in-python/
        s = s.lower()
        for c in [' ', '-', '.', '/']:
            s = s.replace(c, '_')
        s = re.sub('\W', '', s)
        s = s.replace('_', ' ')
        s = re.sub('\s+', ' ', s)
        s = s.strip()
        s = s.replace(' ', '-')
        return s