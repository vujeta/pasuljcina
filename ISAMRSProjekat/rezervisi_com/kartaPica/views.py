from django.shortcuts import render

# Create your views here.
from .models import KartaPica

def svee(request):
	kartePica = KartaPica.objects.all()
	context = {
		"kartePica": kartePica
	}

	return render(request, "spisakKarataPica.html", context)