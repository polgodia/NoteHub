from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from notehub.forms import SignupForm, AddExerciseForm, AddNoteForm, AddExamForm
from django.utils import timezone
from django.urls import reverse
# Create your views here.
from django.views.generic import DetailView

from notehub.models import Student, Document, Exam, Note, Exercise


def home(request):
    template_name = 'notehub/home.html'
    return render(request, template_name, context={'title': 'app_name'})


def documents_list(request):
    documents = Document.objects.all().order_by('id')
    template_name = 'notehub/documents_list.html'
    return render(request, template_name, {'documents': documents})


def exam_list(request):
    exams = Exam.objects.all().order_by('id')
    template_name = 'notehub/exam_list.html'
    return render(request, template_name, {'exams': exams})


def note_list(request):
    notes = Note.objects.all().order_by('id')
    template_name = 'notehub/note_list.html'
    return render(request, template_name, {'notes': notes})


def exercise_list(request):
    exercises = Exercise.objects.all().order_by('id')
    template_name = 'notehub/exercise_list.html'
    return render(request, template_name, {'exercises': exercises})


def document_detail(request, id):
    document = Document.objects.get(id=id)
    return render(request, 'notehub/document_detail.html', {'document': document})
    # return HttpResponse(id)


def user_panel_view(request):
    return render(request, 'notehub/user_panel.html')


@login_required(login_url="/login/")
def add_document_view(request):
    template_name = 'notehub/add_document.html'
    return render(request, template_name, context={'title': 'addDocument'})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notehub:user_panel')
    else:
        form = SignupForm()
    return render(request, 'notehub/signup.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('notehub:user_panel')
    else:
        form = AuthenticationForm()
    return render(request, 'notehub/login.html', context={'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('notehub:list')


def add_exam_view(request):
    if request.method == 'POST':
        form = AddExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            user = get_object_or_404(Student, Q(id=request.user.id))
            exam.creator = user
            exam.save()
            return redirect('notehub:exam_list')
    else:
        form = AddExamForm()
    return render(request, 'notehub/add_Exam.html', context={'form': form})


def add_exercise_view(request):
    if request.method == 'POST':
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            user = get_object_or_404(Student, Q(id=request.user.id))
            exercise.creator = user
            exercise.save()
            return redirect('notehub:exercise_list')
    else:
        print('ERROR')
        form = AddExerciseForm()
    return render(request, 'notehub/add_Exercice.html', context={'form': form})


def add_note_view(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            user = get_object_or_404(Student, Q(id=request.user.id))
            note.creator = user
            note.save()
            return redirect('notehub:note_list')
    else:
        form = AddNoteForm()
    return render(request, 'notehub/add_Note.html', context={'form': form})
