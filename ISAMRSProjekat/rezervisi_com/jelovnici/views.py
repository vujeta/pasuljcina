from django.shortcuts import render

# Create your views here.
from .models import Jelovnik

def svee(request):
	jelovnici = Jelovnik.objects.all()
	context = {
		"jelovnici": jelovnici,

	}
	return render(request, "spisakJelovnika.html", context)