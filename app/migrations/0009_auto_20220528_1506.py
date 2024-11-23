# Generated by Django 3.2.13 on 2022-05-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_uploadcv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='mail',
        ),
        migrations.AddField(
            model_name='chat',
            name='job_user_mail',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_mail',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]