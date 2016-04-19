from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from restorani.models import Restoran
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Jelo(models.Model):
	naziv = models.CharField(max_length = 80)
	opis = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to='jela/images/')
	cena = models.DecimalField(decimal_places=2, max_digits=100)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.naziv

	class Meta:
		unique_together = ('naziv', 'slug')

	def get_absolute_url(self):
		return reverse("single_jelo", kwargs={"slug": self.slug}) #slug

	
def create_slug(instance, new_slug=None):
    slug = slugify(instance.naziv)
    if new_slug is not None:
        slug = new_slug
    qs = Jelo.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Jelo)
