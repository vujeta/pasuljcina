from django.contrib import admin

# Register your models here.
from .models import Restoran

class RestoranAdmin(admin.ModelAdmin):
	class Meta:
		model = Restoran


admin.site.register(Restoran, RestoranAdmin)