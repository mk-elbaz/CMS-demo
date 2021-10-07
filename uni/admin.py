from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(subject)
admin.site.register(Grade)
admin.site.register(Rating)
admin.site.register(Content)
