from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm,VolunteerRegisterForm,IdForm
from .models import Volunteer,City
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from evelist.models import Event,Signup,EventImages
from evelist.models import EventCategory
from datetime import datetime,timedelta,time,date
from django.utils import timezone
import datetime
import random
from django.core.mail import EmailMessage
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		form2=VolunteerRegisterForm(request.POST)
		form3=IdForm(request.POST)
		if form.is_valid() and form2.is_valid():
			new_user=form.save()
			new_volunteer=form2.save(commit=False)
			new_volunteer.user=new_user
			new_volunteer.save()
			hash=str(random.getrandbits(18))
			emailadd=form.cleaned_data['email']
			#emailadd=new_volunteer.user.email
			email=EmailMessage("Your OTP is",hash,to=[emailadd])
			email.send()
			if form3.is_valid():
				idd=form3.cleaned_data['ID']
				#if idd!= None:
				 # new_volunteer.save()
				messages.success(request, f'{new_user} successfully registered now !')
				return redirect('login')
							
			else:
				form3=IdForm(request.POST)
	
			return render(request, 'volunteer/confirm.html',{'form':form3})
	else:
			form = UserRegisterForm()
			form2=VolunteerRegisterForm(request.POST)
			form3=IdForm(request.POST)
	#return redirect('')
		
	return render(request, 'volunteer/register.html', {'form': form,'form2':form2})


@login_required
def profile(request):
	current_user = request.user
	try:
		v=current_user.volunteer
		e=Event.objects.filter(venue=v.my_city,date__range=[datetime.date.today(),"9999-12-31"])
		c=EventCategory.objects.all()
		city=City.objects.all()
		context={
		"Events":e,
		"category" :c,
	    "cityy" :city,
		}
		return render(request,'volunteer/profile.html',context)
	except:
		return render(request,'organization/home.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')


def v_profile(request):
	if request.method == 'GET':
		o_org=request.GET.get('vol')
		c_user=User.objects.filter(username=o_org).first()
		c_vol=Volunteer.objects.filter(user=c_user).first()
		all_events=Event.objects.filter(volunteers=c_vol)
		context={
			"f_name":c_vol.user.first_name,
			"city":c_vol.my_city,
			"l_name":c_vol.user.last_name,
			"events":all_events,
			"Upvotes":c_vol.upvote
		}

	return render(request,"volunteer/v_profile.html",context)

def sort_all(request):
	#all_cat=EventCategory.objects.all()
	all_cat=Event.objects.all()
	context={
		"all":all_cat,}
	return render(request,"evelist/all_city.html",context)


def sort_cat(request):
	if request.method == 'GET':
		cat=request.GET.get('cat')
		ncatagory=EventCategory.objects.filter(category=cat).first()
		geteve=Event.objects.filter(category=ncatagory)
		all_cat=Event.objects.all()
	context={
		"all":geteve,
		
		}
	return render(request,"evelist/cat.html",context)


def sort_city(request):
	
	if request.method == 'GET':
		cit=request.GET.get('jagah')
		#all_city=City.objects.all()
		#if (cit in all_city):
		cur_city=City.objects.filter(name=cit).first()
		ncatagory=Event.objects.filter(venue=cur_city)
		geteve=Event.objects.filter(name=ncatagory)
		all_cat=Event.objects.all()
		
	return render(request,"evelist/cit.html",{
				"all":ncatagory,})	