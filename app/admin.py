from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.



class Usermodel(UserAdmin):
    list_display = ['username','user_type']


admin.site.register(CustomUser,Usermodel)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Session_year)
admin.site.register(Employee_leave)
admin.site.register(Employee_feedback)
admin.site.register(Attendance_report)
admin.site.register(Attendance)
admin.site.register(Staff)
admin.site.register(Register_as_smes)
admin.site.register(Register_as_startUp)
admin.site.register(Staff_feedback)


