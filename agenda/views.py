from django.shortcuts import render

from .models import Agenda


def home(request):
    agenda = Agenda.objects.all()

    context = {
        "agenda": agenda,
    }

    return render(request, 'agenda/agenda.html', context)
