from django.contrib import admin
from notehub import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Document)
admin.site.register(models.Exercise)
admin.site.register(models.Exam)
admin.site.register(models.Note)
admin.site.register(models.Valoration)
