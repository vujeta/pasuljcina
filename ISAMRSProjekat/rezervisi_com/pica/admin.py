from django.contrib import admin

# Register your models here.
from .models import Pice

class PiceAdmin(admin.ModelAdmin):
	class Meta:
		model = Pice


admin.site.register(Pice, PiceAdmin)