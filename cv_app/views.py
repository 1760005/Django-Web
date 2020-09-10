from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import F


# Create your views here.


def index(request):
    email = "ndtanh.17ck1@gmail.com"
    position = 1
    context = None
    if request.POST:
        email = request.POST['email']
        position = ApplyTo.objects.get(name=request.POST['vacancy']).id

    try:
        base_information = BaseInformation.objects.get(email=email)
        educations = Education.objects.filter(user=base_information).order_by(F('end_date').desc())
        certifications = Certification.objects.filter(user=base_information).order_by(F('time').desc())
        activities = Activity.objects.filter(user=base_information).order_by(F('time').desc())
        skills = Skill.objects.filter(user=base_information).order_by(F('id').desc())
        interests = Interest.objects.get(user=base_information)
        projects = Project.objects.filter(user=base_information).order_by(F('time_end').desc())
        apply_to = ApplyTo.objects.get(pk=position)
        context = {'base_information': base_information,
                   'educations': educations,
                   'certifications': certifications,
                   'skills': skills,
                   'activities': activities,
                   'interests': interests,
                   'projects': projects,
                   'apply_to': apply_to,
                   }
    except(KeyError, BaseInformation.DoesNotExist):
        return redirect(setting)
    return render(request, "cv_app/index.html", context)


def setting(request):
    vacancy = ApplyTo.objects.filter()
    context = {
        'vacancy': vacancy,
    }
    return render(request, "cv_app/settings.html", context=context)



