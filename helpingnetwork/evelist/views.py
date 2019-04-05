from django.shortcuts import render,redirect
from organization.models import Organization,OrganizationImages
from .models import Event,EventImages,Signup,Feedback
from django.http import HttpResponse
from .forms import FeForm,NewForm
from django.contrib import messages

#from .forms import EventSignupForm
# Create your views here.
def index(request):
    x=Event.objects.all()
    return render(request, 'evelist/index.html',{'x': x})

def desc(request, event_id):
    x=Event.objects.get(pk=event_id)
    y=x.description
    #return render(request,'evelist')
    return HttpResponse("description: %s" % y)


def printo(request):
	if request.method == 'GET':
		c_event=request.GET.get('event')
		c_org=request.GET.get('org')
		org=Organization.objects.filter(name=c_org).first()
		eventt=Event.objects.filter(name=c_event).first()
		images=EventImages.objects.filter(i_event=eventt)
		context={
         "event":c_event,
         "disp":eventt.description,
         "organizer":eventt.organizer,
         "venue":eventt.venue,
         "date":eventt.date,
         "org":c_org,
			"images":images
		}
	return render(request,'evelist/current_event.html',context)

'''def e_signin(request):
	if request.method == 'POST':
		form2=EventSignupForm(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('change_profile')
	else:
		form2=EventSignupForm()
	return render(request,'evelist/signin_event.html',{'form': form2})
'''

def e_signin(request):

	c_event=request.GET.get('event')
	eventt=Event.objects.filter(name=c_event).first()
	#z=eventt.venue
	current_user = request.user
	y=Event.objects.filter(name=c_event).first()
	z=y.volunteers.all()
	
	if(current_user.volunteer in z):
		messages.warning(request, f'already Signed up for {eventt}!')
	else:	
		v=current_user.volunteer
		#c_org=request.GET.get('org')
		x= Signup(event=eventt,volunteer=v,invite_reason="aisehi")
		x.save()
		messages.success(request, f'successfully Signed up for {eventt}!')

	return redirect('profile')

def pingu(request,form=None):
	if request.method=='GET':
		event=request.GET.get('event')
		getevent=Event.objects.filter(name=event).first()
		if request.method=='POST':
			form=FeForm(request.POST)
			if form.is_valid():
				form.save()
				#return redirect('profile')		
		else:
			form=FeForm()

	
	return render(request,'evelist/something.html',{'something':form})

