from django.shortcuts import render
from .models import ResumeHeader, Summary, TechnicalSkill, Project, Education, Experience, AboutMe


def about_me_view(request):
    about_me = AboutMe.objects.first()
    return render(request, 'personal/about_me.html', {'about_me': about_me})


def resume_view(request):
    header = ResumeHeader.objects.first()
    summary = Summary.objects.first()
    skills = TechnicalSkill.objects.first()
    projects = Project.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()

    context = {
        'ResumeHeader': ResumeHeader,
    }

    return render(request, 'personal/resume.html', context)

