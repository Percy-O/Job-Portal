from django.contrib import admin
from app import models

# Register your models here.

admin.site.register(models.JobCrawl)
admin.site.register(models.Job)
admin.site.register(models.Chat)
admin.site.register(models.AllChat)
