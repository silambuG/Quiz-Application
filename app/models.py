from django.db import models


class TeacherLogin(models.Model):
    User_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


def __str__(self):
    return self.user_name


class StudentDetails(models.Model):
    stud_name = models.CharField(max_length=30)
    stud_roll_no = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    Tamil = models.CharField(max_length=3)
    English = models.CharField(max_length=3)
    Mathematical = models.CharField(max_length=3)
    Science = models.CharField(max_length=3)
    Social_science = models.CharField(max_length=3)
    Hindi = models.CharField(max_length=3)
    Sports = models.CharField(max_length=3)
    Date = models.DateTimeField(auto_now=True)
    Total = models.IntegerField(null=True)


def __str__(self):
    return self.stud_name


class SchoolApplication(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_gender = models.CharField(max_length=10)
    stud_date_of_birth = models.DateField()
    stud_father_name = models.CharField(max_length=30)
    stud_father_mobile = models.CharField(max_length=13)
    stud_mother_name = models.CharField(max_length=30)
    stud_mother_mobile = models.CharField(max_length=13)
    stud_mother_tongue = models.CharField(max_length=20)
    stud_religion = models.CharField(max_length=20)
    stud_caste = models.CharField(max_length=20)
    stud_current_address = models.CharField(max_length=150)
    stud_permanent_address = models.CharField(max_length=150)
    stud_mobile = models.CharField(max_length=13)
    stud_alter_mobile = models.CharField(max_length=13)
    stud_mail = models.EmailField()
    stud_previous_standard = models.CharField(max_length=10)
    stud_previous_mark = models.CharField(max_length=10)
    stud_previous_standard_year = models.DateField()
    stud_join_standard = models.CharField(max_length=10)
    stud_physically_challenged = models.CharField(max_length=10)
    parent_email = models.EmailField()
    apply_date = models.DateField(auto_now=True)
    apply_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.stud_name


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()


class AddQuestion(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200)

    def __str__(self):
        return self.question
