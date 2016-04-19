from django.contrib import admin

# Register your models here.
from .models import Jelo

class JeloAdmin(admin.ModelAdmin):
	search_fields = ['naziv']
	list_display = ['naziv', 'cena']
	list_editable = ['naziv', 'cena']
	list_filter = ['naziv']
	class Meta:
		model = Jelo


admin.site.register(Jelo, JeloAdmin)