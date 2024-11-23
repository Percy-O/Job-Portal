import requests
from bs4 import BeautifulSoup
import time
import os
from app.models import JobCrawl

def crawl():
	
	link = 'https://www.jobberman.com/jobs'
		
	# Get the website content
	get_website = requests.get(link).text

	# BeautifulSoup Plugin
	crawl = BeautifulSoup(get_website,'lxml')

	# Get The Job content
	job_contents = crawl.find_all('div',class_='flex-wrap')

	for job in job_contents:
			
		# 	Getting the link and the job title
		get_links_titles = job.find_all('div',class_='flex items-center')
		job_link=''
		job_title=''
		job_employer=''
		for get_link_title in get_links_titles:
			
			job_link = get_link_title.a['href']
			job_title = get_link_title.find('p',class_='text-brand-linked').text

			# print(f'job link: {job_link}')
			# print(f'job title: {job_title}')


	# 	Getting Who Post The Job
		job_employers = job.find_all('p',class_='text-brand-linked')
		for job_employer in job_employers:
			if job_employer.a is not None:
				job_employer = job_employer.a.text
				# print(f'job employer:{job_employer}')
		
		# Getting Images and description 	
		get_images_and_descriptions = job.find_all('div',class_='basis-full')
		
		for get_image_and_description in get_images_and_descriptions:
			
			job_image = get_image_and_description.find('img',class_='max-w-none')
			job_description = get_image_and_description.find('p',class_='md:pl-5')
			# print(f'job image:{job_image}')
			try:
				# print(f'job description: {job_description.text}')
				None
			except:
				print(job_link)
				print(job_title)
				print(job_employer)
				print(job_image)
				print(job_description)

				save_job = JobCrawl.objects.create(
					user = 'Jobberman',
					job_image=job_image,
					job_title = job_title,
					job_link=job_link,
					job_description = job_description,
					job_employer=job_employer,


				).save()



if __name__ ==' __main__':

	while True:
		crawl()
		time_minute = 2 # 2 Minutes
		print(f'Waiting For {time_minute} minutes...')
		time.sleep(time_minute * 60)