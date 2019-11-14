from django.shortcuts import render
from projects.models import Intro


def project_index(request):
    intros = Intro.objects.all()
    context = {"intros": intros}
    return render(request, "project_index.html", context)
