# Generated by Django 3.2.6 on 2022-05-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220528_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCrawl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('job_image', models.ImageField(blank=True, default='../static/images/job5.jpg', null=True, upload_to='job/image/')),
                ('job_title', models.CharField(max_length=255)),
                ('job_link', models.URLField()),
                ('job_description', models.TextField(max_length=300)),
                ('job_employer', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]