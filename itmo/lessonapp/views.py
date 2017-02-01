from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Lesson, Student, Attendance
from .forms import AttendanceForm


def index(request):
    return render(request, 'lessonapp/index.html')


def students(request):
    return render(request, 'lessonapp/students.html', )


def lessons(request):
    _lessons = Lesson.objects.all()
    return render(request, 'lessonapp/lessons.html', {'lessons': _lessons})


def student(request, student_id):
    return HttpResponse('Student: %s' % student_id)


def lesson(request, lesson_id):
    _lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessonapp/lesson.html', {'lesson': _lesson})


def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        _student = request.POST.get('student')

    else:
        form = AttendanceForm()

    return render(request, 'lessonapp/attendance-form.html', {'form': form})
