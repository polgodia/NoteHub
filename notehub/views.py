from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView

from notehub.models import Student, Document


def home(request):
    template_name = 'notehub/home.html'
    return render(request, template_name, context={'title': 'app_name'})


def register(request):
    template_name = 'notehub/register.html'
    return render(request, template_name, context={'title': 'register'})


def sign_in(request):
    template_name = 'notehub/sign_in.html'
    return render(request, template_name, context={'title': 'sign_in'})

def documents_list(request):
    documents = Document.objects.all().order_by('id')
    template_name = 'notehub/documents_list.html'
    return  render(request,template_name, {'documents': documents})

def document_detail(request, id):
    document = Document.objects.get(id=id)
    return render(request, 'notehub/document_detail.html', {'document':document})
    #return HttpResponse(id)






def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('notehub:list')
    else:
        form = UserCreationForm()
    return render(request, 'notehub/signup.html', context={'form': form})
