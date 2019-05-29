from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	roll = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100,blank=True)
	department = models.CharField(max_length=100)
	phone = models.CharField(max_length=10,blank=True)
	email = models.CharField(max_length=100,blank=True)
	fcmtoken = models.CharField(max_length=500, blank=True)
	lastnotiftime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name 


class Complain(models.Model):
	complainby = models.ForeignKey(User, on_delete=models.CASCADE)
	complain = models.TextField()

	def __str__(self):
		return self.complain

class CouncilandCell(models.Model):
	name = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.name

class Club(models.Model):
	councilname = models.OneToOneField(CouncilandCell, on_delete = models.CASCADE)
	name = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.name

class Notification(models.Model):
	councilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	clubname = models.ForeignKey(Club, null=True, on_delete = models.CASCADE)
	notification = models.CharField(max_length= 1000)
	notification_header = models.CharField(max_length = 100)
	notification_pic = models.ImageField()
	datetime = models.DateTimeField()
	location = models.CharField(max_length = 300)
	view_count = models.IntegerField()
	interested_count = models.IntegerField()

	def __str__(self):
		return self.notification_header


