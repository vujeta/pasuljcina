from django.contrib import admin

# Register your models here.
from .models import Jelovnik

class JelovnikAdmin(admin.ModelAdmin):
	class Meta:
		model = Jelovnik


admin.site.register(Jelovnik, JelovnikAdmin)