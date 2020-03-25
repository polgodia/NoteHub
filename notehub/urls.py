from django.conf.urls import url

from notehub.views import documents_list, document_detail

app_name = 'notehub'

urlpatterns = [
    url(r'^$', documents_list, name='list'),
    url(r'^(?P<id>[\w-]+)/$', document_detail, name="detail")
]
