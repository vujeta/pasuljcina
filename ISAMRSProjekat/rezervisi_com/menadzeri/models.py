from __future__ import unicode_literals

from django.db import models

from restorani.models import Restoran

# Create your models here.

class Menadzer(models.Model):
	restoran = models.ForeignKey(Restoran)
	ime = models.CharField(max_length=120)
	prezime = models.CharField(max_length=120)

	def __unicode__(self):
		return self.prezime