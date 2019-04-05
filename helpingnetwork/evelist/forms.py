from .models import Signup,Feedback
from django import forms


'''class EventSignupForm(forms.ModelForm):
	class Meta:
		model=Signup
		fields=["event","volunteer","invite_reason"]
'''	
class NewForm(forms.Form):
	name=forms.CharField(required=True, label="Feedback")
	
class FeForm(forms.ModelForm):
	class Meta:
		model=Feedback
		fields=["fifa","tfield"]
		
