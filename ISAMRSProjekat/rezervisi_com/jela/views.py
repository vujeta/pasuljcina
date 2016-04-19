from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Jelo
from pica.models import Pice
from jelovnici.models import Jelovnik
from kartaPica.models import KartaPica

from .forms import JeloForm

def svee(request):
	jela = Jelo.objects.all()
	context = {
		"jela": jela
	}

	return render(request, "spisakJela.html", context)



def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		jela = Jelo.objects.filter(naziv__icontains = q)
		if jela:
			context = {

				"trazeno": q, 'jela': jela,
			}
		pice = Pice.objects.filter(naziv__icontains = q)
		if pice:
			context = {

				"trazeno": q, 'pice': pice,
			}

		jelovnici = Jelovnik.objects.filter(naziv__icontains = q)
		if jelovnici:
			context = {

				"trazeno": q, 'jelovnici': jelovnici,
			}

		kartaPica = KartaPica.objects.filter(naziv__icontains = q)
		if kartaPica:
			context = {

				"trazeno": q, 'kartaPica': kartaPica,
			}


		return render(request, "results.html", context)
	else:
		context = {}

		return render(request, "menadzerPocetna.html", context)

def dodaj_jelo(request):
		
	form = JeloForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "napraviJelo.html", context)

def single(request, slug):
	try:
		jelo = Jelo.objects.get(slug=slug)
		#jelo = get_object_or_404(Jelo, slug=slug)
		context = {'jelo': jelo, 'test': "test"}
		return render(request, 'jelo_detalji.html', context)
	except:
		raise Http404

