from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from CMSfinal import settings

urlpatterns = [    
     path('admin/', admin.site.urls),
     path("", views.index, name="index"),
     path("login", views.login_view, name="login"),
     path("logout", views.logout_view, name="logout"),
     path("register", views.register, name="register"),
     path("notAuth", views.notAuth, name="notAuth"),
     path("enroll", views.enroll, name="enroll"),
     path("subjects", views.viewSubjects, name="viewSubjects"),
     path("editSubject", views.editSubjects, name="editSubject"),
     path("getSubjects", views.getSubjects, name="getSubjects"),
     path("ratePage/<int:tutor_id>", views.ratePage, name="ratePage"),
     path("submitRate", views.submitRate, name="submitRate"),
     path("listTutors", views.listTutors, name="listTutors"),
     path("addSubject", views.addSubject, name="addSubject"),
     path("tutorSubjects", views.tutorSubjects, name="tutorSubjects"),
     path("submitGrade", views.submitGrade, name="submitGrade"),
     path("assignTutor", views.assignTutor, name="assignTutor"),
     path("uploadContent/<int:subject_id>", views.uploadContent, name="uploadContent"),
     path("subjectStudents/<int:subject_id>", views.getSubjStudents, name="subjStudents"),
     path("getGrade/<int:subject_id>", views.getGrade, name="getGrade"),
     path("subjectsListContent", views.subjectsListContent, name="subjectsListContent"),

     
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.FILES_URL, document_root= settings.FILES_ROOT)