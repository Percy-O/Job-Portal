from django.db import models
from account.models import User


# Create your models here.

class Job(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	job_image = models.ImageField(upload_to="job/image/",default="../static/images/job5.jpg",null=True,blank=True)
	job_title = models.CharField(max_length=255)
	job_description = models.TextField(max_length=300)
	email = models.EmailField(max_length=255)
	phone_num = models.PositiveIntegerField()
	whatsapp_num = models.PositiveIntegerField()
	status = models.BooleanField(default=False)
	date_posted = models.DateTimeField(auto_now_add = True)
	date_updated = models.DateTimeField(auto_now=True)
	
	
		
	# def save(self,*args,**kwargs):
	# 	self.user=request.user
	# 	super().save(*args,**kwargs)
		
	def __str__(self):
		return f'{self.job_title} - Posted by {self.user.username}'
		
	def job_status(self):
		
		job_given = self.status = True
		
		return job_given
		self.save()
	
class Chat(models.Model):
	user_mail = models.EmailField(max_length=255,null=True)
	job_user= models.ForeignKey(User,on_delete=models.CASCADE)
	job_anonymous = models.CharField(max_length=255,null=True)
	message = models.TextField()
	message_posted = models.DateTimeField(auto_now_add=True)
	message_updated = models.DateTimeField(auto_now=True)

	def __str__(self):

		return f'{self.job_anonymous}'
		
class AllChat(models.Model):
	user_job = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	job_anonymous = models.CharField(max_length=255,null=True)
	chat = models.ManyToManyField(Chat)

	def __str__(self):
		return f'New message of {self.job_anonymous} to {self.user_job.username}'


class UploadCv(models.Model):
	mail = models.CharField(max_length=255)
	cv = models.FileField(upload_to='CV/Upload/')
	job_user = models.ForeignKey(User,on_delete=models.CASCADE)
	date_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return f'{self.mail}'


class JobCrawl(models.Model):
	user = models.CharField(max_length=255)
	job_image = models.ImageField(upload_to="job/image/",default="../static/images/job5.jpg",null=True,blank=True)
	job_title = models.CharField(max_length=255)
	job_link = models.URLField()
	job_description = models.TextField(max_length=300,null=True)
	job_employer = models.CharField(max_length=255)
	date_posted = models.DateTimeField(auto_now_add = True)
	date_updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{self.job_title}'


	
	
	
