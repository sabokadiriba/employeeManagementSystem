from typing import Tuple

from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models import CharField


class CustomUser(AbstractUser):
    USER=(
        (1,'MANAGER'),
        (2,'STAFF'),
        (3,'EMPLOYEE'),
    )

    user_type = models.CharField(choices = USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Session_year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)
    def __str__(self):
        return self.session_start + " to " + self.session_end


class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username




class Employee(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


class Employee_leave(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message=models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.admin.first_name + self.employee_id.admin.last_name




class Employee_notification(models.Model):
    employee_id= models.ForeignKey(Employee,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.Employee_id.admin.first_name


class Staff_notification(models.Model):
    staff_id= models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.staff_id.admin.first_name


class Employee_feedback(models.Model):

    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_replay = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.admin.first_name + self.employee_id.admin.last_name




class Staff_feedback(models.Model):

    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_replay = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name


class Attendance(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    attendance_data = models.DateField()
    session_year_id = models.ForeignKey(Session_year, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_id.name



class Attendance_report(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.admin.first_name





class Register_as_smes(models.Model):
    campany = models.CharField(max_length=100)
    campany_type = models.TextField()
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    grand_father_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    kebele = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    p_o_box = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    tin = models.CharField(max_length=100)
    registasion_date = models.DateField()
    vat_no = models.CharField(max_length=100)
    about_title=models.TextField()
    field= models.TextField()
    proposal = models.FileField(upload_to="media/file")

    def __str__(self):
        return self.campany



class Register_as_startUp(models.Model):
    campany = models.CharField(max_length=100)
    campany_type = models.TextField()
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    grand_father_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    kebele = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    p_o_box = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    tin = models.CharField(max_length=100)
    registasion_date = models.DateField()
    vat_no = models.CharField(max_length=100)
    about_title=models.TextField()
    field= models.TextField()
    proposal = models.FileField(upload_to="media/file")

    def __str__(self):
        return self.campany

