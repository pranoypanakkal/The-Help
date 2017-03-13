from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/', include('profiles.urls' , namespace="profiles")),
    url(r'^', include('home.urls', namespace="home")),
    url(r'^users/', include('users.urls', namespace="users")),
]
