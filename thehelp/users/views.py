from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .forms import UserForm
from .models import Worker


class UserFormView(View):
    template_name = 'users/user_form.html'
    form_class = UserForm

    def get(self, request, *args):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return home(request, user.id)
        return render(request, self.template_name, {'form': form})



def login_user(request):
    username = request.GET.get('user')
    password = request.GET.get('pass')
    user = authenticate(username=username, password=password)

    if user is not None:

        if user.is_active:
            login(request, user)
        return home(request, user.id)



def logout_view(request):
    logout(request)
    return redirect('users:index')


def index(request):
    template = loader.get_template('users/home.html')
    return HttpResponse(template.render(request))


def search(request):
    x = request.GET.get('x')
    all_workers = Worker.objects.filter(skills__contains=x)
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))


class login_view(View):
    template_name = 'users/home.html'
    form_class = UserForm

    def get(self, request, *args):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args):
        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return home(request, user.id)
        return render(request, self.template_name, {'form': form})

def electrical(request):
    all_workers = Worker.objects.filter(skills__contains="electrical")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers,
    }
    return HttpResponse(template.render(context, request))

def Plumbing(request):
    all_workers = Worker.objects.filter(skills__contains="Plumbing")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def Carpentry(request):
    all_workers = Worker.objects.filter(skills__contains="Carpentry")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def Cleaning(request):
    all_workers = Worker.objects.filter(skills__contains="Cleaning")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def Painting(request):
    all_workers = Worker.objects.filter(skills__contains="Painting")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def Builder(request):
    all_workers = Worker.objects.filter(skills__contains="Builder")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def Electronic(request):
    all_workers = Worker.objects.filter(skills__contains="Electronic")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def PestControl(request):
    all_workers = Worker.objects.filter(skills__contains="PestControl")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))

def WeldingFabrication(request):
    all_workers = Worker.objects.filter(skills__contains="Welding")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))
def Flooring(request):
    all_workers = Worker.objects.filter(skills__contains="Flooring")
    template = loader.get_template('profiles/profileList.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))






#after login


def home(request, user_id):
    user = User.objects.get(pk=user_id)
    template = loader.get_template('users/index.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))


def search_login(request, user_id):
    x = request.GET.get('x')
    all_workers = Worker.objects.filter(skills__contains=x)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers, }
    return HttpResponse(template.render(context, request))


def electrical_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="electrical")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Plumbing_login(request,user_id):
    all_workers = Worker.objects.filter(skills__contains="Plumbing")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Carpentry_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Carpentry")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Cleaning_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Cleaning")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Painting_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Painting")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Builder_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Builder")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Electronic_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Electronic")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def PestControl_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="PestControl")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def WeldingFabrication_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Welding")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def Flooring_login(request, user_id):
    all_workers = Worker.objects.filter(skills__contains="Flooring")
    user = User.objects.get(pk=user_id)
    template = loader.get_template('profiles/profileListlogin.html')
    context = {
        'all_workers': all_workers,
        'user': user,
    }
    return HttpResponse(template.render(context, request))
