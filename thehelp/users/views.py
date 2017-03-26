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


def home(request, user_id):
    template = loader.get_template('users/index.html')
    user = User.objects.get(pk=user_id)

    context = {
        'user': user, }
    return HttpResponse(template.render(context, request))

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
