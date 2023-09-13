from django.db import models

from django.db import models

class ResumeHeader(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField()
    github = models.URLField()

class Summary(models.Model):
    text = models.TextField()

class TechnicalSkill(models.Model):
    languages = models.TextField()
    tools_and_skills = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    github_link = models.URLField()
    description = models.TextField()
    technologies_used = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255, blank=True, null=True)

class Experience(models.Model):
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Null for current jobs
    responsibilities = models.TextField()

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


# Create your models here.
