from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<worker_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'worker/add/$', views.WorkerCreate.as_view(), name='worker-add'),
]
