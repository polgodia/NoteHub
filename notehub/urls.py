from django.conf.urls import url

from notehub.views import documents_list, document_detail, user_panel, add_document_view, add_exam_view, \
    add_exercise_view, add_note_view

app_name = 'notehub'

urlpatterns = [
    url(r'^$', documents_list, name='list'),
    url(r'^(?P<id>[\w-]+)/$', document_detail, name="detail"),
    url(r'^userpanel/', user_panel, name='userpanel'),
    url(r'^addDocument/', add_document_view, name='addDocument'),
    url(r'^addExam/', add_exam_view, name='addExam'),
    url(r'^addExercise/', add_exercise_view, name='addExercise'),
    url(r'^addNote/', add_note_view, name='addNote'),
]
