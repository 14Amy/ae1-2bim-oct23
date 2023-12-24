from django.shortcuts import render

from .models import Pais, Barrio


def pais(request):
    latest_pais_list = Pais.objects.order_by("-pub_date")[:5]
    context = {"latest_pais_list": latest_pais_list}
    return render(request, "polls/pais.html", context)


def barrio(request):
    latest_barrio_list = Barrio.objects.all()[:5]
    context = {"latest_barrio_list": latest_barrio_list}
    return render(request, "polls/barrio.html", context)