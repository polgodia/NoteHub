from django.conf.urls import url

from notehub.views import documents_list, document_detail, add_document_view, user_panel_view, add_exam_view, \
    add_exercise_view, add_note_view, add_exercice_simple

app_name = 'notehub'

urlpatterns = [
    url(r'^document_list', documents_list, name='list'),
    url(r'^user_panel', user_panel_view, name='user_panel'),
    url(r'^addDocument/', add_document_view, name='addDocument'),
    url(r'^addExam/', add_exam_view, name='addExam'),
    url(r'^addExercise/', add_exercise_view, name='addExercise'),
    url(r'^addNote/', add_note_view, name='addNote'),
    #url(r'^(?P<id>[\w-]+)/$', document_detail, name='detail') #always last
]
