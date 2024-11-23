from django.urls import path
from app import views


urlpatterns = [

	path('dashboard/',views.dashboard,name='dashboard'),
	path('add/job',views.add_job,name='add_job'),
	path('all/job',views.all_job,name='all_job'),
	path('update/<int:id>/job',views.update_job,name='update_job'),

	path('all/message/',views.get_chat,name='all_message'),
	path('message/<int:id>',views.chat_bot,name='message'),
	path('all/cv/',views.all_cv,name='all_cv'),

	path('webcrawler',views.crawl,name='crawl')
	
	
]