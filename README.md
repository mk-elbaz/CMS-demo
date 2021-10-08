# CMS-demo

Uni Portal is a small-scale online university content and grade management system, you can register and login as one of three roles:

### Admin:

Can view tutor average ratings.

Can Add, Edit subjects.

Assign tutor to subject.

View students enrolled in subjects.

### Tutor:

Can only be assigned to one subject.

Can check which subject is assigned to him.

Can check students enrolled in his subject.

Can add and update grades of his students.

Upload course content to be available for students.

### Student:

Can check all subjects he's enrolled in. (Only superuser can enroll students in subjects)

Can check subject description and tutor assigned to it.

Can download content available for each subject.

Can check grade assigned to each subject.

Can rate or edit rate for tutors of each subject.

### Applicant:

It's not a role you can register with but you can apply to the university ,filling all the needed info and submitting it for the admin to see it through the admin django interface.

### File uploads and downloads:

Uploaded files are stored in a folder in the root directory named 'files', which is also accessed to download files.

## How to open the project:

-After cloning the github repository, make sure you got python installed.

Open the terminal in the project directory and run the following commands:

​	-python3 manage.py makemigrations uni

​	-python3 manage.py migrate

​	-python3 manage.py runserver

To create django superuser:

​	-python3 manage.py createsuperuser 

To run tests.py file:

​	-python3 manage.py test

## Hope you enjoy!!

