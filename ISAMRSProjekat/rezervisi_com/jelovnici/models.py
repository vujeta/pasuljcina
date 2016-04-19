from __future__ import unicode_literals

from django.db import models
from jela.models import Jelo
# Create your models here.

class Jelovnik(models.Model):
	naziv = models.CharField(max_length = 80)
	jela = models.ManyToManyField(Jelo, blank=True)

	def __unicode__(self):
		return self.naziv