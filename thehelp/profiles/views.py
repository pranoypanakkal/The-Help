from django.http import HttpResponse
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from .models import Worker

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

def worker_add(request):
	template = loader.get_template('profiles/signup.html')
	return HttpResponse(template.render(request))


class WorkerCreate(CreateView):
	model = Worker
	fields = ['name', 'ph_number', 'email', 'address', 'age', 'gender']



