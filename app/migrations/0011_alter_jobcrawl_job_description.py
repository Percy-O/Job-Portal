# Generated by Django 3.2.6 on 2022-05-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_jobcrawl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcrawl',
            name='job_description',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]