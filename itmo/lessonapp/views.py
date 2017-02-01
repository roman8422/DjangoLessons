from django.shortcuts import render, get_object_or_404, \
    redirect
from django.http import HttpResponse, Http404
from .models import Lesson, Student, Attendance
from .forms import AttendanceForm


def index(request):
    return render(request, 'lessonapp/index.html')


def students(request):
    _students = Student.objects.all()
    return render(request, 'lessonapp/students.html',  {'students': _students})


def lessons(request):
    _lessons = Lesson.objects.all()
    return render(request, 'lessonapp/lessons.html', {'lessons': _lessons})


def student(request, student_id):
    _student = Student.objects.get(pk=student_id)
    return render(request, 'lessonapp/student.html', {'student': _student})


def lesson(request, lesson_id):
    _lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessonapp/lesson.html', {'lesson': _lesson})


def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        _student = request.POST.get('student')
        _lesson = request.POST.get('lesson')
        _attendance = Attendance(
            student=Student.objects.get(pk=_student),
            lesson=Lesson.objects.get(pk=_lesson)
        )
        _attendance.save()
        return redirect('lessonapp:student', student_id=_student)
    else:
        form = AttendanceForm()

    return render(request, 'lessonapp/attendance-form.html', {'form': form})
