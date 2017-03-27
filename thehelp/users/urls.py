from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [
      
        url(r'^register$', views.UserFormView.as_view(), name='register'),
        url(r'^home(?P<user_id>[0-9]+)',views.home, name='home'),
        url(r'^logout$',views.logout_view, name='logout'),
        url(r'^electrical(?P<user_id>[0-9]+)',views.electrical_login, name='electrical'),
        url(r'^Plumbing(?P<user_id>[0-9]+)',views.Plumbing_login, name='Plumbing'),
        url(r'^Carpentry(?P<user_id>[0-9]+)',views.Carpentry_login, name='Carpentry'),
        url(r'^Cleaning(?P<user_id>[0-9]+)',views.Cleaning_login, name='Cleaning'),
        url(r'^Painting(?P<user_id>[0-9]+)',views.Painting_login, name='Painting'),
        url(r'^Builder(?P<user_id>[0-9]+)',views.Builder_login, name='Builder'),
        url(r'^Electronic(?P<user_id>[0-9]+)',views.Electronic_login, name='Electronic'),
        url(r'^PestControl(?P<user_id>[0-9]+)',views.PestControl_login, name='PestControl'),
        url(r'^Welding&Fabrication(?P<user_id>[0-9]+)',views.WeldingFabrication_login, name='Welding&Fabrication'),
        url(r'^Flooring(?P<user_id>[0-9]+)',views.Flooring_login, name='Flooring'),
        url(r'^search(?P<user_id>[0-9]+)',views.search_login, name='search'),
        url(r'^electrical',views.electrical, name='electrical'),
        url(r'^Plumbing',views.Plumbing, name='Plumbing'),
        url(r'^Carpentry',views.Carpentry, name='Carpentry'),
        url(r'^Cleaning',views.Cleaning, name='Cleaning'),
        url(r'^Painting',views.Painting, name='Painting'),
        url(r'^Builder',views.Builder, name='Builder'),
        url(r'^Electronic',views.Electronic, name='Electronic'),
        url(r'^PestControl',views.PestControl, name='PestControl'),
        url(r'^Welding&Fabrication',views.WeldingFabrication, name='Welding&Fabrication'),
        url(r'^Flooring',views.Flooring, name='Flooring'),
        url(r'^search',views.search, name='search'),
        url(r'^login',views.login_user, name='login'),
        url(r'^',views.index, name='index'),

]