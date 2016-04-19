from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from restorani.models import Restoran
# Create your models here.

class Jelo(models.Model):
	naziv = models.CharField(max_length = 80)
	opis = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to='jela/images/')
	cena = models.DecimalField(decimal_places=2, max_digits=100)

	def __unicode__(self):
		return self.naziv

	def get_absolute_url(self):
		return reverse("jela:jelo_detalji", kwargs={"id": self.id})



