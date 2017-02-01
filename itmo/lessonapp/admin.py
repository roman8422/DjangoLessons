from django.contrib import admin
from .models import Lesson, Student, Attendance

admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Attendance)
