from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Restoran(models.Model):
	naziv = models.CharField(max_length = 80)
	vrsta = models.CharField(max_length = 80)

	def __unicode__(self):
		return self.naziv


	

