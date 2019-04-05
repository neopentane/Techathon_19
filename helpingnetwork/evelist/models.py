from django.db import models
from django.contrib.auth.models import User
from volunteer.models import City,Volunteer
from django.utils import timezone
from organization.models import Organization

class EventCategory(models.Model):
	category=models.CharField(max_length=100)
	def __str__(self):
		return self.category

class Event(models.Model):
	category=models.ForeignKey(EventCategory,on_delete=models.CASCADE)
	volunteers= models.ManyToManyField(Volunteer,through='Signup')
	name=models.CharField(max_length=100)
	description=models.TextField()
	organizer=models.ForeignKey(Organization,on_delete=models.CASCADE)
	venue=models.ForeignKey(City,on_delete=models.CASCADE)
	date=models.DateTimeField()
	eventprofileImage=models.ImageField(default='default.jpg', upload_to='eventprofileImage')
	def __str__(self):
		return self.name
class Signup(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	invite_reason = models.CharField(max_length=64)
	def __str__(self):
		return self.invite_reason

class EventImages(models.Model):
	i_event=models.ForeignKey(Event,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg', upload_to='eventimages')

class Feedback(models.Model):
	fifa=models.ForeignKey(Event,on_delete=models.CASCADE)
	tfield=models.CharField(max_length=100)
# Create your models here.

