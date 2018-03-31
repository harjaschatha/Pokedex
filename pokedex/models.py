from django.db import models


class Pokemon(models.Model):
	dex = models.CharField(primary_key=True, max_length=3)
	img = models.URLField()
	name = models.CharField(max_length=200)
	types = models.CharField(max_length=200)
	species = models.CharField(max_length=200)
	height = models.CharField(max_length=200)
	weight = models.CharField(max_length=200)

	def __str__(self):
		return '{}'.format(self.name)


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


# class Ability(models.Model):
# 	ability1 = models.CharField(max_length = 200)
# 	ab1_desc = models.CharField(max_length = 400)
# 	ability2 = models.CharField(max_length = 200)
# 	ab2_desc = models.CharField(max_length = 400)
# 	hiddenab = models.CharField(max_length = 200)
# 	hiddenab_desc = models.CharField(max_length = 400)