# Generated by Django 3.2.13 on 2022-05-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_image',
            field=models.ImageField(default='../static/images/job5.jpg', null=True, upload_to='job/image/'),
        ),
    ]
