from django.conf.urls import url
from . import views

app_name = 'lessonapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.students, name='students'),
    url(r'^lessons/$', views.lessons, name='lessons'),
    url(r'^lesson/(?P<lesson_id>[0-9]+)/$', views.lesson, name='lesson'),
    url(r'student/(?P<student_id>[0-9]+)/$', views.student, name='student'),
    url(r'^attendance/$', views.attendance, name='attendance')
]
