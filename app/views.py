from django.db import transaction
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from app import models,forms

# Create your views here.

def dashboard(request):

	jobs = models.Job.objects.filter(user=request.user)
	context={'jobs':jobs}
	return render(request,'app/dashboard.html',context)

def add_job(request):
	
	form = forms.JobForm()
	if request.method == 'POST':

		# Get Job Details
		user = request.user
		job_image = request.FILES.get('job_image')
		job_title = request.POST.get('job_title')
		job_description = request.POST.get('job_description')
		email = request.POST.get('email')
		phone_num = request.POST.get('phone_num')
		whatsapp_num = request.POST.get('whatsapp_num')

		job_form = models.Job.objects.create(

				user = user,
				job_image = job_image,
				job_title = job_title,
				job_description = job_description,
				email = email,
				phone_num = phone_num,
				whatsapp_num = whatsapp_num
		)
		job_form.save()

		if job_form  is not None:
			messages.success(request,'Job Successfully Posted')
		else:
			messages.error(request,'Unable to Post Job')
		
		
	context={'form':form}
	return render(request,'app/addjob.html',context)

def all_job(request):
	
	jobs = models.Job.objects.all()

	
	context = {'jobs':jobs}
	return render(request,'app/alljob.html',context)


def update_job(request,id):
	
	get_job = models.Job.objects.get(id=id)
	form = forms.JobForm(instance=get_job)
	
	if request.method == 'POST':
# 		Get Job Details
		user = request.user
		job_image = request.FILES.get('job_image')
		job_title = request.POST.get('job_title')
		job_description = request.POST.get('job_description')
		email = request.POST.get('email')
		phone_num = request.POST.get('phone_num')
		whatsapp_num = request.POST.get('whatsapp_num')
		
# 		Update Job Details
		get_job.user = user
		get_job.job_image = job_image
		get_job.job_title = job_title
		get_job.job_description = job_description
		get_job.email = email
		get_job.phone_num = phone_num
		get_job.whatsapp_num = whatsapp_num
# 		Save Updated Job Details
		get_job.save()
		
		if get_job:
			messages.success(request,'Job Details Updated Successfully!')
		else:
			messages.error(request,"Unable tp Update Job Details ")
			
	
	context = {'form':form}
	return render(request,'app/addjob.html',context)


def get_chat(request):
	# All Messages
	messages = models.AllChat.objects.all()
	# Get the last message

	
	context = {'messages':messages}
	return render(request,'app/get_message.html',context)
	
def chat_bot(request,id):

	message = models.AllChat.objects.get(id=id)
	job_anonymous = message.job_anonymous
	if request.method == 'POST':
		
		# Anonymous Mail
		mail = request.user.email
		# Job User
		job_user = request.user
		# Message
		message = request.POST.get('message')

		# Save Message
		send_message = models.Chat.objects.create(
			user_mail = mail,
			job_user = job_user,
			job_anonymous=job_anonymous,
			message=message,
		)
		send_message.save()

		# Get Chat User
		chats = models.Chat.objects.filter(job_anonymous=job_anonymous)
		get_user_chat = models.AllChat.objects.get(job_anonymous=job_anonymous,user_job=request.user)
		# Add All Messages of the user
		for chat in chats:
			get_user_chat.chat.add(chat)
		return HttpResponseRedirect(f'{id}' )




	context={'message':message,'job':job_anonymous}
	return render(request,'app/message.html',context)


def all_cv(request):

	# All CV
	cvs = models.UploadCv.objects.filter(job_user=request.user)

	context={'cvs':cvs}
	return render(request,'app/allcv.html',context)


import requests
from bs4 import BeautifulSoup
import time
import os


def crawl(request):
	with transaction.atomic():
		job_link = []
		job_title = []
		job_employer = []
		job_description = []
		job_image=[]
		if request.method== 'POST':
			link = request.POST.get('url')
			# link = 'https://www.jobberman.com/jobs?page=2'
				
			# Get the website content
			get_website = requests.get(link).text

			# BeautifulSoup Plugin
			crawl = BeautifulSoup(get_website,'lxml')

			# Get The Job content
			job_contents = crawl.find_all('div',class_='flex-wrap')
			# Getting All Content
			employer = ''
			title=''
			link=''
			for job in job_contents:
					
				# 	Getting the link and the job title
				get_links_titles = job.find_all('div',class_='flex items-center')

				for get_link_title in get_links_titles:
					# Get Link
					link = get_link_title.a['href']
					# Get Title
					title = get_link_title.find('p',class_='text-brand-linked').text
					# Job Link
					try: 
						job_link.append(link)
					except:
						pass
					# Job Title
					try:
						job_title.append(title)
					except:
						pass


			# 	Getting Who Post The Job
				job_employers = job.find_all('p',class_='text-brand-linked')
				for employer in job_employers:
					try:
						employer = employer.a.text
						# Job Employer
						job_employer.append(employer)
					except:
						pass
						
				
				# Getting Images and description 	
				get_images_and_descriptions = job.find_all('div',class_='basis-full')
				
				for get_image_and_description in get_images_and_descriptions:
					# Get Image
					image = get_image_and_description.find('img',class_='max-w-none')

					if image is not None:
						# Image
						job_image.append(image)

					# Get Description
					description = get_image_and_description.find('p',class_='md:pl-5')

					try:
						# Description
						job_description.append(description.text)
						# desc = description.text
					except:
						pass

					
					# print(employer)
					# print(image)

			jobs=zip(job_link,job_title,job_employer,job_description)

			crawl_job = [
					models.JobCrawl(

						user = 'Jobberman',
						job_link = job[0],
						job_title=job[1],
						job_employer=job[2],
						job_description =job[3])
						for job in jobs

					]
			models.JobCrawl.objects.bulk_create(crawl_job)
			messages.success(request,'Job Successfully Crawled!!!')	

					
					
						
			# jobs=zip(job_link,job_title,job_employer,job_description)
				
			# for job_link,job_title,job_employer,job_description in jobs:
			# 	# with open('employer.txt','a+') as emp:
			# 	# 		get = emp.write(f'Job:{job_link}\n{job_title}\n{job_employer}\n{job_image}\n{job_description}\n')


			# 	# Get Job
			# 	try: 
			# 		check_job= models.JobCrawl.objects.get(
			# 						job_title = job_title,
			# 		)
			# 	except:

			# 		# Save Job If Not Exists
			# 		save_job = models.JobCrawl.objects.create(
			# 				user = 'Jobberman',
			# 				job_title = job_title,
			# 				job_employer=job_employer,
			# 				job_link=job_link,
			# 				job_description = job_description
							
			# 		)
			# 		save_job.save()	
			# 		messages.success(request,'Job Successfully Crawled!!!')	
			# 	else:

			# 		# Check If It Exists
			# 		messages.error(request,f'{check_job.job_title} exists!')

				

	return render(request,'app/jobcrawl.html')






		
		