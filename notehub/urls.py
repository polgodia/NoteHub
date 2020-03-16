from django.conf.urls import url

from notehub.views import documents_list, register, sign_in, signup_view

app_name = 'notehub'

urlpatterns = [
    url(r'^register/', register, name='notehub'),
    url(r'^sign_in/', sign_in, name='notehub'),
    url(r'^signup/', signup_view, name='notehub'),
    url(r'^$', documents_list)
]