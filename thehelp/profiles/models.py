from django.db import models
from django.core.urlresolvers import reverse


class Worker(models.Model):
			name = models.CharField(max_length=100)
			ph_number = models.IntegerField()
			email = models.CharField(max_length=100)
			address = models.CharField(max_length=250)
			password = models.CharField(max_length=100)
			age = models.IntegerField()
			skills = models.CharField(max_length=500)
			Profile_pic = models.CharField(max_length=1000)
			gender = models.CharField(max_length=15)
			hire = models.CharField(max_length=20)
			state = models.CharField(max_length=20)
			city = models.CharField(max_length=50)
			request = models.CharField(max_length=50)

			def get_absolute_url(self):
				return reverse('profiles:index')



