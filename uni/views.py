from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import fields
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from django import forms


from .models import *

# Create your views here.
class newApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ['fullName','birthDate','email','grade','faculty','nationality']
        widgets = {
            'fullName' : forms.TextInput(attrs={'class': 'form-control'}),
            'birthDate' : forms.DateInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'grade' : forms.TextInput(attrs={'class': 'form-control'}),
            'faculty' : forms.Select(attrs={'class': 'form-select'}),
            'nationality' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class newContentUploadForm(ModelForm):
    class Meta:
        model = Content
        fields = ['name','file']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'file' : forms.FileInput(attrs={'class': 'form-control'})
        }

def index(req):
    return render(req, "uni/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "uni/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "uni/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def notAuth(req):
    return render(req, "uni/notAuth.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        role = request.POST["role"]
        if role == "None":
            return render(request, "uni/register.html", {
                "message": "Please choose role."
            })

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "uni/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.role = role
            user.save()
        except IntegrityError:
            return render(request, "uni/register.html", {
                "message": "username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "uni/register.html")


def enroll(req):
    if req.method == "POST":
        form = newApplicantForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            return render(req, "uni/index.html",{
                "message" : "Successfully Applied!"
            })
        else:
            return render(req, "uni/enroll.html", {
                "form": form
            })
    else:
        return render(req, "uni/enroll.html", {
            "form": newApplicantForm()
        })

@login_required
def viewSubjects(req):
    if req.user.role != "c":
        return HttpResponseRedirect(reverse("notAuth"))
    subj = subject.objects.all()
    t = getAvailableTutors(req)
    return render(req,"uni/newSubject.html",{
        "subjects" : subj,
        "teacher" : t
    })

@login_required
def addSubject(req):
    if req.user.role != "c":
        return HttpResponseRedirect(reverse("notAuth"))
    if req.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    body = json.loads(req.body)  
    name = body['name']
    desc = body['description']
    subj = subject(
        name = name,
        description = desc,
        tutor = None,
    )
    subj.save()
    return JsonResponse({"message": "subject added successfully."}, status=201)


@login_required
def editSubjects(req):
    if req.user.role != "c":
        return HttpResponseRedirect(reverse("notAuth"))
    if req.method == 'POST':
        body = json.loads(req.body)     
        id = int(body['id'])
        subj = subject.objects.get(id = id)  
        newName = body['name']
        desc = body['description']
        subj.name = newName
        subj.description = desc
        subj.save()
        return JsonResponse({"message": "Subject updated successfully."}, status=201)

@login_required
def assignTutor(req):
    if req.user.role != "c":
        return HttpResponseRedirect(reverse("notAuth"))
    if req.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    body = json.loads(req.body)  
    subjName = body['sName']
    tutorName = body['tName']
    subj = subject.objects.get(name = subjName)
    tutor = User.objects.get(username = tutorName)
    subj.tutor = tutor
    subj.save()
    tutor.save()    
    return JsonResponse({"message": "Tutor added successfully."}, status=201)



@login_required
def getAvailableTutors(req):
    teachers = User.objects.filter(role = 'b',assignedSubject = None )
    return teachers

@login_required
def getSubjStudents(req, subject_id):
    if req.user.role == "a":
        return HttpResponseRedirect(reverse("notAuth"))
    subj = subject.objects.get(id = subject_id)
    students = User.objects.filter(subjectStudents = subject_id)
    return render(req,"uni/studentsList.html",{
        "students" : students,
        "subject" : subj,
    })

@login_required
def getSubjects(req):
    student = User.objects.get(id = req.user.id)
    subjects = subject.objects.filter(students = student)
    
    return render(req,"uni/subjectsList.html",{
        "subjects" : subjects
    })

@login_required
def subjectsListContent(req):
    student = User.objects.get(id = req.user.id)
    subjects = subject.objects.filter(students = student)
    
    return render(req,"uni/subjectsListContent.html",{
        "subjects" : subjects
    })


@login_required
def ratePage(req,tutor_id):
    if req.user.role != "a":
        return HttpResponseRedirect(reverse("notAuth"))
    tutor = User.objects.get(id = tutor_id)
    return render(req,"uni/rateTutor.html",{
            'tutor': tutor
    })
    
@login_required
def submitRate(req):
    if req.user.role != "a":
        return HttpResponseRedirect(reverse("notAuth"))
    if req.method == 'POST':
        body = json.loads(req.body)
        rate = int(body['rate'])
        tutorName = body['tutor']
        student = User.objects.get(id = req.user.id)
        tutor = User.objects.get(username = tutorName)
        newRatingBool = Rating.objects.filter(student = student, tutor = tutor).exists()
        if newRatingBool:
            updateRating = Rating.objects.get(student = student, tutor = tutor)
            updateRating.rate = rate
            updateRating.save()
            return JsonResponse({"message": "Tutor rating updated successfully."}, status=201)
        newRating = Rating(
            tutor = tutor,
            rate = rate,
            student = student
        )
        newRating.save()
        return JsonResponse({"message": "Tutor rating added successfully."}, status=201)

@login_required
def listTutors(req):
    if req.user.role != "c":
        return HttpResponseRedirect(reverse("notAuth"))
    tutors = User.objects.filter(role = "b").all()
    return render(req,"uni/tutorsList.html",{
            'tutors': tutors
    })

@login_required
def tutorSubjects(req):
    if req.user.role != "b":
        return HttpResponseRedirect(reverse("notAuth"))
    subjects = subject.objects.filter(tutor = req.user).all()
    return render(req,"uni/tutorSubjects.html",{
            'subjects': subjects
    })

@login_required
def submitGrade(req):
    if req.user.role != "b":
        return HttpResponseRedirect(reverse("notAuth"))
    if req.method == 'POST':
        body = json.loads(req.body)
        grade = int(body['grade'])
        subjID = int(body['subjID'])
        studentID = int(body['studentID'])
        student = User.objects.get(id = studentID)
        subj = subject.objects.get(id = subjID)
        gradeObjBool = Grade.objects.filter(student = student, subject = subj).exists()
        if gradeObjBool:
            gradeObj = Grade.objects.get(student = student, subject = subj)
            gradeObj.value = grade
            gradeObj.save()
            return JsonResponse({"message": "Grade updated successfully."}, status=201)
        newGrade = Grade(
            value = grade,
            subject = subj,
            student = student
        )
        newGrade.save()
        return JsonResponse({"message": "Grade added successfully."}, status=201)

@login_required
def getGrade(req,subject_id):
    if req.user.role != "a":
        return HttpResponseRedirect(reverse("notAuth"))
    student = User.objects.get(id = req.user.id)
    subj = subject.objects.get(id = subject_id)
    if not Grade.objects.filter(student = student,subject = subj).exists():
        return JsonResponse("No grade uploaded yet", safe=False)
    grade = Grade.objects.get(student = student,subject = subj)
    gradeValue = grade.value
    return JsonResponse(gradeValue, safe=False)

@login_required
def uploadContent(req,subject_id):
    if req.user.role != "b":
        return HttpResponseRedirect(reverse("notAuth"))
    subj = subject.objects.get(id = subject_id)
    if req.method == "POST":    
        form = newContentUploadForm(req.POST , req.FILES)
        if form.is_valid():
            newContent = form.save(commit=False)
            newContent.subject = subj
            newContent.file = form.cleaned_data['file']
            newContent.save()
            return HttpResponseRedirect(reverse('tutorSubjects'))
        else:
            return render(req, "uni/upload.html" , {
                "form" : form,
                
            })   
    else:
        return render(req, "uni/upload.html" , {
                "form" : newContentUploadForm(),
                "subject" : subj
        }) 