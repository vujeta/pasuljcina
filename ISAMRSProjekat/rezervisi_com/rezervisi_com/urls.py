"""rezervisi_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'menadzeri.views.home', name='menadzerPocetna'),
    url(r'^jela/$', 'jela.views.svee', name='jela'),
    url(r'^pica/$', 'pica.views.svee', name='pica'),
    url(r'^jelovnici/$', 'jelovnici.views.svee', name='jelovnici'),
    url(r'^kartaPica/$', 'kartaPica.views.svee', name='kartaPica'),
    url(r'^restorani/$', 'restorani.views.svee', name='restorani'),
    url(r'^dodaj_jelo/$', 'jela.views.dodaj_jelo', name='dodaj_jelo'),
    url(r'^s/$', 'jela.views.search', name='search'),
    url(r'^jela/(?P<slug>[\w-]+)/$', 'jela.views.single', name='single_jelo'),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)