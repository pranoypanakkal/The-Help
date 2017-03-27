from django.http import HttpResponse
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from .models import Worker
from django.contrib.auth.models import User

def index(request):
	all_workers = Worker.objects.all()
	template = loader.get_template('profiles/profileList.html')
	context = {
	      'all_workers': all_workers,}
	return HttpResponse(template.render(context, request))


def detail(request, worker_id):
	template = loader.get_template('profiles/profile.html')
	worker = Worker.objects.get(pk=worker_id)

	context = {
	       'worker': worker,}

	return HttpResponse(template.render(context, request))


def detail_login(request, worker_id, user_id):
	template = loader.get_template('profiles/profilelogin.html')
	user = User.objects.get(pk=user_id)
	worker = Worker.objects.get(pk=worker_id)

	context = {
	       'worker': worker,
	       'user'  : user,
	       }

	return HttpResponse(template.render(context, request))



class WorkerCreate(CreateView):
	model = Worker
	fields = ['name', 'ph_number', 'email', 'address', 'age', 'gender', 'state', 'password', 'city', 'skills']
























