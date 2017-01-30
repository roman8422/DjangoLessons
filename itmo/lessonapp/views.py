from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")


def students(request):
    return HttpResponse('Students')


def lessons(request):
    return HttpResponse('Lessons')


def student(request, student_id):
    return HttpResponse('Student: %s' % student_id)


def lesson(request, lesson_id):
    return HttpResponse('Lesson: %s' % lesson_id)
