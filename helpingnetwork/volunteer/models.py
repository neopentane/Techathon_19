from django.db import models
from django.contrib.auth.models import User

#hello this is priyaa
# Create your models here.
class City(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Volunteer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	my_city=models.ForeignKey(City,on_delete=models.CASCADE)
	upvote = models.IntegerField(default=0)
	myid = models.CharField(max_length=100,default="Zz3edcvuji876ty")
	def __str__(self):
		return f'{self.user.username} '


		
