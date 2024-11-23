import requests
from bs4 import BeautifulSoup
import time
import os
# from app.models import Job


# link = 'https://www.jobberman.com/jobs'

# # Get the website content
# get_website = requests.get(link).text

# # BeautifulSoup Plugin
# crawl = BeautifulSoup(get_website,'lxml')

# # Get The Job content
# job_contents = crawl.find_all('div',class_='flex-wrap')

# for job_content in job_contents:
# 	job_header = job_content.find_all('div',class_='w-full')
# 	for job in job_header:
		
# 		# 	Getting the link and the job title
# 		get_links_titles = job.find_all('div',class_='flex items-center')
		
# 		for get_link_title in get_links_titles:
			
# 			job_link = get_link_title.a['href']
# 			job_title = get_link_title.find('p',class_='text-brand-linked').text
	
# 			print(f'job link: {job_link}')
# 			print(f'job title: {job_title}')


# 	# 	Getting Who Post The Job
# 		job_employers = job.find_all('p',class_='text-brand-linked')
# 		for job_employer in job_employers:
# 			if job_employer.a is not None:
# 				job_employer = job_employer.a.text
# 				print(f'job employer:{job_employer}')
	
# 	# Getting Images and description 	
# 	get_images_and_descriptions = job_content.find_all('div',class_='basis-full')
	
# 	for get_image_and_description in get_images_and_descriptions:
		
# 		job_image = get_image_and_description.find('img',class_='max-w-none')
# 		job_description = get_image_and_description.find('p',class_='md:pl-5')
# 		print(f'job image:{job_image}')
# 		try:
# 			print(f'job description: {job_description.text}')
# 		except:
# 			pass

image = ['image1','image2','image3','image4','image5','image6']
employer = ['employer1','employer2','employer3','employer4','employer5','employer6']
description = ['description1','description2','description3','description4','description5','description6']

jobs = zip(image,employer,description)

for image,employer,description in jobs:

	print (image,employer,description)

