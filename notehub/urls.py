from django.conf.urls import url

from notehub.views import documents_list, document_detail, add_document_view, user_panel_view, add_exam_view, \
    add_exercise_view, add_note_view, exam_list, exercise_list, note_list, valorate_view

app_name = 'notehub'

urlpatterns = [
    url(r'^$', user_panel_view, name='user_panel'),
    url(r'^document_list', documents_list, name='list'),
    url(r'^exam_list', exam_list, name='exam_list'),
    url(r'^exercise_list', exercise_list, name='exercise_list'),
    url(r'^note_list', note_list, name= 'note_list'),
    url(r'^addDocument/', add_document_view, name='addDocument'),
    url(r'^addExam/', add_exam_view, name='addExam'),
    url(r'^addExercise/', add_exercise_view, name='addExercise'),
    url(r'^addNote/', add_note_view, name='addNote'),
    url(r'^(?P<id>[\w-]+)/$', document_detail, name='detail'), #always last
    url(r'^(?P<id>[\w-]+)/valorate/$', valorate_view, name='valorate'),
]
