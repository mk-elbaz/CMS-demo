# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


FACULTIES = (
    ('a', "None"),
    ('b', "Computer Science"),
    ('c', "Business"),
    ('d', "Engineering"),
    ('e', "Design"),
    ('f', "Medicine"),
    ('g', "Applied Arts")
)

ROLES = (
    ('a', "student"),
    ('b', "tutor"),
    ('c', "admin"),
)

# https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLES, null=False, blank=False)

    @property
    def getRole(self):
        r = dict(ROLES)
        return r[self.role]

    def getRate(self):
        return Rating.getAvgRating(self, self)

    def getGrade(self, subject):
        # student = User.objects.get(id =)
        return Grade.getGrade(self, self, subject)


class Applicant(models.Model):
    fullName = models.CharField(max_length=100)
    birthDate = models.DateField()
    email = models.EmailField(blank=False)
    grade = models.CharField(max_length=2)
    faculty = models.CharField(
        max_length=1, default=FACULTIES[0][1], choices=FACULTIES, blank=False, null=False)
    nationality = models.CharField(max_length=20)


class subject(models.Model):
    name = models.CharField(max_length=50, default='None', unique=True)
    description = models.CharField(max_length=300)
    tutor = models.OneToOneField(User, blank=True, null=True, default='None',
                                 on_delete=models.CASCADE, related_name='assignedSubject')
    students = models.ManyToManyField(
        'User', default=None, blank=True, related_name='subjectStudents')

    def getContent(self):
        return Content.objects.filter(subject = self).all()

class Grade(models.Model):
    student = models.ForeignKey(
        User, blank=False, on_delete=models.CASCADE, related_name='studentGrade')
    subject = models.ForeignKey(
        subject, blank=False, on_delete=models.CASCADE, related_name='subjGrade')
    value = models.FloatField()

    def getGrade(self, student, subject):
        g = Grade.objects.get(student=student, subject=subject)
        return g.value

    def serialize(self): {
        "gradeValue": self.value
    }


class Rating(models.Model):
    rate = models.IntegerField(default=0, validators=[MaxValueValidator(5),
                                                      MinValueValidator(1)])
    student = models.ForeignKey(
        'User', default=None, blank=False, on_delete=models.CASCADE, related_name='studentRating')
    tutor = models.ForeignKey(
        'User', default=None, blank=False, on_delete=models.CASCADE, related_name='tutorRating')

    def getAvgRating(self, tutor):
        if not Rating.objects.filter(tutor=tutor).exists():
            return 0
        return int(Rating.objects.filter(tutor=tutor).all().aggregate(Avg('rate'))['rate__avg'])


class Content(models.Model):
    name = models.CharField(max_length=100,blank= False)
    file = models.FileField(upload_to='files', blank=False)
    subject = models.ForeignKey(
        subject, null=False, blank=False, on_delete=models.CASCADE, related_name="content")
