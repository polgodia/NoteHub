from django.conf.urls import url

from notehub.views import documents_list, document_detail, add_document_view, user_panel_view

app_name = 'notehub'

urlpatterns = [
    url(r'^document_list', documents_list, name='list'),
    url(r'^user_panel', user_panel_view, name='user_panel'),
    url(r'^add_document', add_document_view, name='add_document'),
    url(r'^(?P<id>[\w-]+)/$', document_detail, name='detail')
]
