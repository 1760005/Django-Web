from django.db import models


# Create your models here.


class BaseInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True, unique=True)

    gender_choice = (
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other")
    )
    gender = models.CharField(max_length=7, choices=gender_choice)
    career_objectives = models.TextField(blank=True)
    about = models.TextField(blank=True)


class Education(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    GPD = models.FloatField(default=0)


class Activity(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateField()
    place = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    mission = models.CharField(max_length=200, blank=True)


class Certification(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateField()


class Skill(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)


class Interest(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


class Project(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time_start = models.DateField()
    time_end = models.DateField()
    skill = models.CharField(max_length=400)
    content = models.CharField(max_length=200)
    position = models.CharField(max_length=50, blank=True)


class ApplyTo(models.Model):
    name = models.CharField(max_length=100, unique=True)
