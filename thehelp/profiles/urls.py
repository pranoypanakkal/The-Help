from django.conf.urls import url
from . import views

app_name = 'profiles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<worker_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^register/$', views.worker_add, name='worker_add'),
]
