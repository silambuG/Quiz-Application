
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mark_entry', views.student_marks, name='student_marks'),
    path('student_result', views.student_result, name='student_result'),
    path('application_form', views.application_form, name='application_form'),
    path('student_result_login', views.student_result_login, name='student_result_login'),
    path('staff_login', views.staff_login, name='staff_login'),
    path('about_us', views.about_us, name='about_us'),
    path('staff_signup', views.staff_sign_up, name='staff_signup'),
    path('quiz', views.quiz, name='quiz'),
    path('take_quiz', views.take_quiz, name='take_quiz'),
    path('add_question', views.add_question, name='add_question'),
    path('multi_quiz', views.multi_quiz, name='multi_quiz'),
    path('computer_science_quiz', views.computer_science_quiz, name='computer_science_quiz'),
    path('sports_quiz', views.sports_quiz, name='sports_quiz'),
    path('gk_quiz', views.gk_quiz, name='gk_quiz'),
    path('history_quiz', views.history_quiz, name='history_quiz'),
]
