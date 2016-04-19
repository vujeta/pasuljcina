from django.shortcuts import render

# Create your views here.
from .models import Restoran

def svee(request):
	restorani = Restoran.objects.all()
	context = {
		"restorani": restorani
	}

	return render(request, "spisakRestorana.html", context)