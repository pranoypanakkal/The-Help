from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from .models import Worker

def index(request):
	all_workers = Worker.objects.all()
	template = loader.get_template('profiles/profileList.html')
	context = {
	      'all_workers': all_workers,
	}
	return HttpResponse(template.render(context, request))

def detail(request, album_id):
	return HttpResponse("<h2>Details for album id:" + str(worker_id) + "</h2>")

class WorkerCreate(CreateView):
	model = Worker
	fields = ['name', 'ph_number', 'email', 'address', 'age', 'skills', 'gender']