from django import forms
from app import models

class JobForm(forms.ModelForm):
	
	class Meta:
		
		model = models.Job
		exclude = ['status','date_updated','date_posted']
		fields = '__all__'