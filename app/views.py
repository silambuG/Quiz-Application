from django.shortcuts import render
from django.contrib import messages
from .models import *
import requests, json


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        teacher_login_data = TeacherLogin(User_name=username, password=password)
        teacher_login_data.save()
    return render(request, 'school_main.html', {})


def student_marks(request):
    if request.method == 'POST':
        stud_name = request.POST['student_name']
        roll_no = request.POST['stud_roll_no']
        date_of_birth = request.POST['date_of_birth']
        tamil = request.POST['Tamil']
        english = request.POST['English']
        maths = request.POST['Mathematical']
        science = request.POST['Science']
        social_science = request.POST['Social_science']
        hindi = request.POST['Hindi']
        sports = request.POST['Sports']
        total = int(tamil) + int(english) + int(maths) + int(science) + int(social_science)
        print(total)
        add_details = StudentDetails(stud_name=stud_name, stud_roll_no=roll_no, date_of_birth=date_of_birth, Tamil=tamil, English=english, Mathematical=maths, Science=science, Social_science=social_science, Hindi=hindi, Sports=sports, Total=total)
        add_details.save()
    return render(request, 'students_details.html', {})


def staff_sign_up(request):
    return render(request, 'staff_signup.html', {})


def staff_login(request):
    return render(request, 'staff_login.html', {})


def student_result_login(request):
    return render(request, 'student_result_login.html', {})


def student_result(request):
    if request.method == "POST":
        roll_no = request.POST['stud_roll_no']
        dob = request.POST['date_of_birth']
        result = StudentDetails.objects.filter(stud_roll_no=roll_no, date_of_birth=dob)
    return render(request, 'stud_result.html', {'result': result})


def application_form(request):
    if request.method == 'POST':
        stud_name = request.POST['stud_name']
        gender = request.POST['sex']
        stud_dob = request.POST['dob']
        father = request.POST['father_name']
        father_ph_no = request.POST['father_mobile']
        mother = request.POST['mother_name']
        mother_ph_no = request.POST['mother_mobile']
        mother_tongue = request.POST['mother_tongue']
        religion = request.POST['religion']
        caste = request.POST['caste']
        current_address = request.POST['current_address']
        permanent_address = request.POST['permanent_address']
        stud_mob = request.POST['stud_ph_no']
        stud_alter_no = request.POST['stud_alter_ph_no']
        stud_mail = request.POST['stud_mail']
        stud_previous_stand = request.POST['previous_stand']
        mark = request.POST['previous_mark']
        year_of_passing = request.POST['passed_out']
        joining_stand = request.POST['join_stand']
        physical = request.POST['physically_challenged']
        parent_mail_id = request.POST['parent_mail']
        app_data = SchoolApplication(stud_name=stud_name, stud_gender=gender, stud_date_of_birth=stud_dob,
                                     stud_father_name=father, stud_father_mobile=father_ph_no, stud_mother_name=mother,
                                     stud_mother_mobile=mother_ph_no, stud_mother_tongue=mother_tongue,
                                     stud_religion=religion, stud_caste=caste, stud_current_address=current_address,
                                     stud_permanent_address=permanent_address, stud_mobile=stud_mob,
                                     stud_alter_mobile=stud_alter_no, stud_mail=stud_mail,
                                     stud_previous_standard=stud_previous_stand, stud_previous_mark=mark,
                                     stud_previous_standard_year=year_of_passing, stud_join_standard=joining_stand,
                                     stud_physically_challenged=physical, parent_email=parent_mail_id)
        app_data.save()
    return render(request, 'school_application.html', {})


def form_download(request):
    pdfkit.from_url('', 'application.pdf')
    return render(request, 'pdf_download.html', {})


def about_us(request):
    return render(request, 'about_us.html', {})


def image(request):
    form = Image.objects.all()
    return render(request, 'image.html', {'form': form})


def add_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        option_1 = request.POST['Option_1']
        option_2 = request.POST['Option_2']
        option_3 = request.POST['Option_3']
        option_4 = request.POST['Option_4']
        answer = request.POST['answer']
        explanation = request.POST['explanation']
        ques_info = AddQuestion(question=question, option_1=option_1, option_2=option_2,
                                option_3=option_3, option_4=option_4, answer=answer, explanation=explanation)
        print(ques_info)
        ques_info.save()
    return render(request, 'quizz_question.html')


def quiz(request):
    return render(request, 'quizz.html', {})


def take_quiz(request):
    questions = AddQuestion.objects.all()
    return render(request, 'take_quiz.html', {'question': questions})


def multi_quiz(request):
    return render(request, 'multiple_quiz.html', {})


def computer_science_quiz(request):
    computer_ques_api = requests.get("https://opentdb.com/api.php?amount=20&category=18&type=multiple")
    data = json.loads(computer_ques_api.content)
    # print(data)
    return render(request, 'computer_science_quiz.html', {'data': data})


def sports_quiz(request):
    sports_ques_api = requests.get("https://opentdb.com/api.php?amount=20&category=21&type=multiple")
    data = json.loads(sports_ques_api.content)
    # print(data)
    return render(request, 'sports_quiz.html', {'data': data})


def gk_quiz(request):
    gk_ques_api = requests.get("https://opentdb.com/api.php?amount=20&category=9&type=multiple")
    data = json.loads(gk_ques_api.content)
    # print(data)
    return render(request, 'gk_quiz.html', {'data': data})


def history_quiz(request):
    history_quiz_api = requests.get("https://opentdb.com/api.php?amount=20&category=23&type=multiple")
    data = json.loads(history_quiz_api.content)
    # print(data)
    return render(request, 'history_quiz.html', {'data': data})
