from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pica.models import Pice

class KartaPica(models.Model):
	naziv = models.CharField(max_length = 80)
	pica = models.ManyToManyField(Pice, blank=True)

	def __unicode__(self):
		return self.naziv