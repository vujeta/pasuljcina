from __future__ import unicode_literals

from django.db import models

from restorani.models import Restoran

# Create your models here.

class Pice(models.Model):
	naziv = models.CharField(max_length = 80)
	opis = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to='pica/images/')
	cena = models.DecimalField(decimal_places=2, max_digits=100)

	def __unicode__(self):
		return self.naziv
