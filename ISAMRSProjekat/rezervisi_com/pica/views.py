from django.shortcuts import render

# Create your views here.
from .models import Pice

def svee(request):
	pica = Pice.objects.all()
	context = {
		"pica": pica
	}

	return render(request, "spisakPica.html", context)