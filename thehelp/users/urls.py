from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [
      
        url(r'^register$', views.UserFormView.as_view(), name='register'),
        url(r'^logout$',views.logout_view, name='logout'),
        url(r'^search',views.search, name='search'),
        url(r'^login',views.login_user, name='login'),
        url(r'^',views.index, name='index'),

]