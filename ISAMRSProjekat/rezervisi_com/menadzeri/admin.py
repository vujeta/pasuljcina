from django.contrib import admin

# Register your models here.
from .models import Menadzer

class MenadzerAdmin(admin.ModelAdmin):
	class Meta:
		model = Menadzer


admin.site.register(Menadzer, MenadzerAdmin)

