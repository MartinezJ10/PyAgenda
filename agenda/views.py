from django.shortcuts import render, redirect

from .models import Agenda
from .forms import CreateContact


def home(request):
    agenda = Agenda.objects.all()

    form = CreateContact(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "agenda": agenda,
        "form": form,
    }

    return render(request, 'agenda/agenda.html', context)


def deleteContact(request, pk):
    contact = Agenda.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("/")
