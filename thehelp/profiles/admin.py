from django.contrib import admin
from .models import Worker
from .models import User

admin.site.register(Worker)
admin.site.register(User)
