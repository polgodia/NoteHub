from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from notehub.models import Student


def intro(request):
    template_name = 'notehub/base.html'
    return render(request,template_name,context={'title': 'app_name'})


