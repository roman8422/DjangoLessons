from django.db import models
from django.db.models import CharField, DateTimeField, TextField, \
    DateField, ForeignKey


class Student(models.Model):
    name = CharField(max_length=100)
    created_at = DateTimeField()


class Lesson(models.Model):
    theme = CharField(max_length=100)
    description = TextField()
    date = DateField()


class Attendance(models.Model):
    student = ForeignKey(Student, on_delete=models.CASCADE)
    lesson = ForeignKey(Lesson, on_delete=models.CASCADE)
    created_at = DateTimeField()
