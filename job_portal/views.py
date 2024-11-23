from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from app import models
from account.models import User

def home(request):

	jobs = models.Job.objects.all()

	crawlsjobs = models.JobCrawl.objects.all()
	
	# Get Page 1
	page = request.GET.get('page_crawl_job',1)

	# Data Per Page
	paginator = Paginator(crawlsjobs, 12)

	try:
		crawljobs = paginator.page(page)
	except PageNotAnInteger:
		crawljobs = paginator.page(1)
	except EmptyPage:
		crawljobs = paginator.page(paginator.num_pages)

	# Get Page 1
	page = request.GET.get('page_job',1)

	# Data Per Page
	paginatorjob = Paginator(jobs, 4)

	try:
		jobs = paginatorjob.page(page)
	except PageNotAnInteger:
		jobs = paginatorjob.page(1)
	except EmptyPage:
		jobs = paginatorjob.page(paginatorjob.num_pages)


	# context={'jobs':jobs,'crawlsjobs':crawlsjobs}
	context={'jobs':jobs,'crawljobs':crawljobs,'crawlsjobs':crawlsjobs}
	return render(request,'home.html',context)

def get_job(request,title):

	job = models.Job.objects.get(job_title=title)
	context={'job':job}
	return render(request,'job_details.html',context)



def chat_bot(request,id):

	job = models.Job.objects.get(id=id)

	# Get Message
	messages = models.Chat.objects.filter(job_user__username=job.user.username,job_anonymous=request.session.get('mail'))

	# get user mail
	mail = request.session.get('mail')

	# Get Job User For Cv
	jobuser = User.objects.get(username=job.user.username)
	request.session['jobuser']=jobuser.username

	if request.method == 'POST':

		if request.session.get('mail'):
			mail = request.session.get('mail')
		else:
			mail = request.POST.get('mail')

		# Anonymous Mail
		request.session['mail'] = mail

		job_user = User.objects.get(username=job.user.username)
		job_anonymous = mail
		# User Session
		message = request.POST.get('message')

		# Save Message
		send_message = models.Chat.objects.create(
			user_mail = mail,
			job_user = job_user,
			job_anonymous = job_anonymous,
			message=message,
		)
		send_message.save()

		
		chats = models.AllChat.objects.filter(job_anonymous=job_anonymous)

		if not chats.exists():
			allchat = models.AllChat.objects.create(job_anonymous=mail,user_job=job_user).save()

		# Get Chat User
		chats = models.Chat.objects.filter(job_anonymous=job_anonymous)
		get_user_chat = models.AllChat.objects.get(job_anonymous=job_anonymous)
		# Add All Messages of the user
		for chat in chats:
			get_user_chat.chat.add(chat)

		# Redirect to the same page
		return HttpResponseRedirect(f'{id}')



	context = {'job':job,'messages':messages,'mail':mail}
	return render(request,'chatbot.html',context)


def upload_cv(request):

	job_user_username = request.session.get('jobuser')
	if request.method == 'POST':

		cv = request.FILES.get('cv')
		mail = request.session.get('mail')
		job_user = User.objects.get(username=job_user_username)
		# Upload Cv

		save_cv = models.UploadCv.objects.create(

				cv= cv,
				mail = mail,
				job_user = job_user
		)
		save_cv.save()

		if save_cv:
			messages.success(request,f'{mail}, Your CV is Uploaded Successfully')
		else:
			messages.error(request,f'{mail},Unable to Upload CV')

	context={'job_user_username':job_user_username}
	return render(request,'uploadcv.html',context)

