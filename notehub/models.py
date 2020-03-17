from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


# Create your models here.

class Student(User):
    DNI = models.CharField(max_length=20, unique=True)
    degree = models.CharField(max_length=50)
    starting_date = models.DateField()
    #subjects = models.TextField()
    average_valoration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return u"%s" % self.username

    #def get_absolute_url(self):
     #   return reverse('myrestaurants:dish_detail',
     #                  kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})


class Document(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    degree = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    last_update = models.DateField(default=date.today)
    average_valoration = models.IntegerField(default=0)

    def __str__(self):
        return u"%s" % self.degree + " | " + self.subject + " | " + self.name

    #def get_absolute_url(self):
     #   return reverse('notehub:document',
      #                 kwargs={'pkr': self.document.pk, 'pk': self.pk})


class Exercice(Document):
    unit = models.IntegerField()
    corrected = models.BooleanField(default=False)


class Exam(Document):
    PARCIAL_NUMBER = ((1, 'First'), (2, 'Second'))
    date = models.DateField()
    parcial = models.PositiveSmallIntegerField(choices=PARCIAL_NUMBER)
    exercices = models.ManyToManyField(Exercice)
    solved = models.BooleanField(default=False)


class Note(Document):
    POSSIBLE_DEGREES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    unit = models.IntegerField()
    date = models.DateField()
    schematization_degree = models.PositiveSmallIntegerField(blank=False, choices=POSSIBLE_DEGREES)


class Valoration(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField(blank=False, choices=RATING_CHOICES)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return u"%s" % "Valoration " + str(self.id) + " of " + self.document.name