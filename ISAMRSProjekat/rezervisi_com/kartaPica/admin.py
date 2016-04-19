from django.contrib import admin

# Register your models here.

from .models import KartaPica

class KartaPicaAdmin(admin.ModelAdmin):
	class Meta:
		model = KartaPica


admin.site.register(KartaPica, KartaPicaAdmin)