# Generated by Django 3.2.13 on 2022-05-25 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_image', models.ImageField(default='../static/job5.jpg', null=True, upload_to='job/image/')),
                ('job_title', models.CharField(max_length=255)),
                ('job_description', models.TextField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('phone_num', models.PositiveIntegerField()),
                ('whatsapp_num', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('message_posted', models.DateTimeField(auto_now_add=True)),
                ('message_updated', models.DateTimeField(auto_now=True)),
                ('job_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
