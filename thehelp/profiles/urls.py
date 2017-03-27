from django.conf.urls import url
from . import views

app_name = 'profiles'

urlpatterns = [
    url(r'^(?P<worker_id>[0-9]+)/(?P<user_id>[0-9]+)',views.detail_login, name='detail_login'),
    url(r'^profile(?P<worker_id>[0-9]+)/(?P<user_id>[0-9]+)',views.profile, name='facebook'),
    url(r'^(?P<worker_id>[0-9]+)',views.detail, name='detail'),
    url(r'^register$', views.WorkerCreate.as_view(), name='worker_add'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^auth', views.auth, name="auth"),
    url(r'^$', views.index, name='index'),
]
 