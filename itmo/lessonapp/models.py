import datetime
from django.db import models
from django.db.models import CharField, DateTimeField, TextField, \
    DateField, ForeignKey


class Student(models.Model):
    name = CharField(max_length=100)
    created_at = DateTimeField()

    def __str__(self):
        return '{}'.format(self.name)


class Lesson(models.Model):
    theme = CharField(max_length=100)
    description = TextField()
    date = DateField()

    def __str__(self):
        return '{}'.format(self.theme)


class Attendance(models.Model):
    student = ForeignKey(Student, on_delete=models.CASCADE)
    lesson = ForeignKey(Lesson, on_delete=models.CASCADE)
    created_at = DateTimeField(default=datetime.datetime.now)
