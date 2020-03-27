from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from notehub.forms import SignupForm, AddExamForm, AddExerciseForm, AddNoteForm
from django.utils import timezone

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


def return_view(request):
    template_name = 'notehub/user_panel.html'
    return render(request, template_name, context={'title': 'return'})


def documents_list(request):
    documents = Document.objects.all().order_by('id')
    template_name = 'notehub/documents_list.html'
    return render(request, template_name, {'documents': documents})


def document_detail(request, id):
    document = Document.objects.get(id=id)
    return render(request, 'notehub/document_detail.html', {'document': document})
    # return HttpResponse(id)


def add_document_view(request):
    template_name = 'notehub/add_document.html'
    return render(request, template_name, context={'title': 'addDocument'})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notehub:list')
    else:
        form = SignupForm()
    return render(request, 'notehub/signup.html', context={'form': form})


def add_exam_view(request):
    if request.method == 'POST':
        form = AddExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notehub:list')
    else:
        form = AddExamForm()
    return render(request, 'notehub/add_document.html', context={'form': form})


def add_exercise_view(request):
    if request.method == 'POST':
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notehub:list')
    else:
        form = AddExerciseForm()
    return render(request, 'notehub/add_document.html', context={'form': form})


def add_note_view(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notehub:list')
    else:
        form = AddNoteForm()
    return render(request, 'notehub/add_document.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notehub/user_panel.html')
    else:
        form = AuthenticationForm()
    return render(request, 'notehub/login.html', context={'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('notehub:list')
