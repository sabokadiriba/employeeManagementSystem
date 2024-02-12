from django.shortcuts import render,redirect,HttpResponse
from app.models import CustomUser,Session_year,Department,Employee,Employee_leave,Employee_notification,Staff_notification,Employee_feedback,Staff_feedback,Staff,Attendance_report,Attendance,Register_as_smes,Register_as_startUp

from django.contrib import messages




def MANAGER_HOME(request):
    department=Department.objects.all().count()
    employee = Employee.objects.all().count()
    eleave=Employee_leave.objects.filter().count()
    feedback=Employee_feedback.objects.all().count()
    enotification=Employee_notification.objects.filter().count()
    snotification = Employee_notification.objects.filter().count()

    staff=Staff.objects.all().count()
    context={
        'department':department,
        'employee':employee,
        'staff':staff,
        'eleave':eleave,
        'feedback':feedback,
        'enotification':enotification,
        'snotification': snotification,
    }
    return render(request, 'Manager/manager_home.html',context)



def ADD_EMPLOYEE(request):
    department=Department.objects.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "email is already taken")
            return redirect('add_employee')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "username is already taken")
            return redirect('add_employee')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,

            )

            user.set_password(password)
            user.save()


            employee = Employee(
                admin=user,
                address=address,
                gender=gender,
                department_id=department,
            )
            employee.save()
            messages.success(request, ' Employe is registered saccussfuly ')
            return redirect('add_employee')
    context={
        'department':department
    }
    return render(request,'Manager/add_employee.html',context)


def VIEW_EMPLOYEE(request):
    employee = Employee.objects.all()
    context={
        'employee':employee
    }
    return render(request,'Manager/view_employee.html',context)


def MANAGER_UPDATE_EMPLOYEE_INFO(request,id):
    employee=Employee.objects.filter(id=id)
    dictionary={
        'employee':employee,
    }
    return render(request,'Manager/update_employee_info.html',dictionary)


def MANAGER_SAVE_EMPLOYEE_INFO(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=employee_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic

        user.save()

        employee = Employee.objects.get(admin=employee_id)
        employee.gender = gender
        employee.address = address
        employee.save()
        messages.success(request, 'employee is successfully updated')
        return redirect('view_employee')

    return render(request,'Manager/view_employee.html')


def MANAGER_DELETE_EMPLOYEE(request,admin):
    employee=CustomUser.objects.get(id=admin)

    employee.delete()
    messages.success(request, 'deleted successfully')
    return redirect('view_employee')



def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "email is already taken")
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "username is already taken")
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2,

            )

            user.set_password(password)
            user.save()


            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, 'registered saccussfuly ')
            return redirect('add_staff')

    return render(request,'Manager/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff
    }
    return render(request, 'Manager/view_staff.html', context)


def MANAGER_UPDATE_STAFF_INFO(request,id):
    staff = Staff.objects.filter(id=id)
    dictionary = {
        'staff': staff,
    }
    return render(request, 'Manager/update_staff_info.html', dictionary)


def MANAGER_SAVE_STAFF_INFO(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()
        messages.success(request, 'staff is successfully updated')
        return redirect('view_staff')

    return render(request, 'Manager/view_staff.html')


def MANAGER_DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)

    staff.delete()
    messages.success(request, 'deleted successfully')
    return redirect('view_staff')


def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session = Session_year(
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request, ' session is successfully added')
        return redirect('add_session')
    return render(request,'Manager/add_session.html')


def VIEW_SESSION(request):
    session = Session_year.objects.all()
    context = {
        'session': session
    }
    return render(request, 'Manager/view_session.html ',context)


def MANAGER_UPDATE_SESSION(request,id):
    session = Session_year.objects.filter(id=id)

    context = {
        'session': session,

    }
    return render(request, 'Manager/update_session.html', context)


def MANAGER_SAVE_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session_id = request.POST.get('session_id')

        session = Session_year.objects.get(id=session_id)
        session.session_start=session_year_start
        session.session_end = session_year_end
        session.save()

        messages.success(request, ' session is successfully updated')
        return redirect('view_session')

    return render(request, 'Manager/view_session.html')


def MANAGER_DELETE_SESSION(request,id):
    session=Session_year.objects.get(id=id)
    session.delete()
    messages.success(request,'session is successfully deleted')
    return redirect('view_session')


def ADD_DEPARTMENT(request):
    if request.method == 'POST':
        department_name = request.POST.get('department_name')
        department = Department(
            name=department_name
        )
        department.save()
        messages.success(request, "your are added succassfully")
    return render(request, 'Manager/add_department.html ')

def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        'department': department
    }
    return render(request, 'Manager/view_department.html ', context)



def MANAGER_UPDATE_DEPARTMENT(request,id):
    department = Department.objects.get(id=id)
    context = {
        'department': department
    }
    return render(request, 'Manager/update_department.html ', context)


def MANAGER_SAVE_DEPARTMENT(request):
    if request.method == "POST":
        department_name = request.POST.get('department_name')
        department_id = request.POST.get('department_id')

        department = Department.objects.get(id=department_id)
        department.name = department_name
        department.save()

        messages.success(request, ' department is successfully updated')
        return redirect('view_department')

    return render(request, 'Manager/view_department.html')


def MANAGER_DELETE_DEPARTMENT(request,id):
    department=Department.objects.get(id=id)
    department.delete()
    messages.success(request,'department deleted successfully')
    return redirect('view_department')


def VIEW_EMPLOYEE_LEAVE(request):
    employee_leave = Employee_leave.objects.all()
    context = {
        'employee_leave': employee_leave,
    }
    return render(request, 'Manager/view_employee_leave.html', context)

def APPROVE_EMPLOYEE_LEAVE(requist,id):
    leave = Employee_leave.objects.get(id=id)
    leave.status=1
    leave.save()
    return redirect('view_employee_leave')


def DISAPPROVE_EMPLOYEE_LEAVE(requist,id):
    leave = Employee_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('view_employee_leave')







def SEND_NOTIFICATION_TO_EMPLOYEE(request):
    employee = Employee.objects.all()
    see_notification = Employee_notification.objects.all().order_by('-id')

    context = {
        'employee':employee,
        'see_notification': see_notification,
    }

    return render(request, 'Manager/send_notification_to_employee.html', context)


def SAVE_NOTIFICATION_OF_EMPLOYEE(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        message = request.POST.get('message')

        employee = Employee.objects.get(admin=employee_id)

        notification = Employee_notification(
            employee_id=employee,
            message=message,
        )
        notification.save()
        messages.success(request, 'notification is sent successfully')
        return redirect('send_notification_to_employee')

def SEND_NOTIFICATION_TO_STAFF(request):
    staff = Staff.objects.all()
    see_notification = Staff_notification.objects.all().order_by('-id')

    context = {
        'staff': staff,
        'see_notification': see_notification,
    }

    return render(request, 'Manager/send_notification_to_staff.html', context)


def SAVE_NOTIFICATION_OF_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)

        notification = Staff_notification(
            staff_id=staff,
            message=message,
        )
        notification.save()
        messages.success(request, 'notification is sent successfully')
    return redirect('send_notification_to_staff')


def REPLY_EMPLOYEE_FEEDBACK(request):
    employee = Employee.objects.all()
    feedback = Employee_feedback.objects.all()

    context = {
        'employee': employee,
        'feedback': feedback,
    }
    return render(request,'Manager/reply_employee_feedback.html',context)


def SAVE_EMPLOYEE_FEEDBACK_REPLY(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_replay = request.POST.get('feedback_replay')
        print(feedback_replay, feedback_id)
        feedback = Employee_feedback.objects.get(id=feedback_id)
        print(feedback)
        feedback.feedback_replay = feedback_replay
        feedback.save()
        messages.success(request, 'feedback is sent successfully')
        return redirect('manager_reply_employee_feedback')




def REPLY_STAFF_FEEDBACK(request):
    staff = Staff.objects.all()
    feedback = Staff_feedback.objects.all()

    context = {
        'staff': staff,
        'feedback': feedback,
    }
    return render(request, 'Manager/reply_staff_feedback.html', context)


def SAVE_STAFF_FEEDBACK_REPLY(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_replay = request.POST.get('feedback_replay')
        feedback = Staff_feedback.objects.get(id=feedback_id)
        feedback.feedback_replay = feedback_replay
        feedback.save()
        messages.success(request, 'notification is sent successfully')
        return redirect('manager_reply_staff_feedback')


def MANAGER_VIEW_ATTENDANCE(request):
    session_year = Session_year.objects.all()
    department = Department.objects.all()
    action = request.GET.get('action')

    get_department = None
    get_session_year = None
    attendance_report = None
    attendance_date = None

    if action is not None:
        if request.method == "POST":
            department_id = request.POST.get('department_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_department = Department.objects.get(id=department_id)
            get_session_year = Session_year.objects.get(id=session_year_id)

            attendance = Attendance.objects.filter(department_id=get_department, attendance_data=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_report.objects.filter(attendance_id=attendance_id)

    context = {
        'department': department,
        'session_year': session_year,
        'action': action,
        'get_department': get_department,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,

    }
    return render(request,'Manager/view_attendance.html',context)


def MANAGER_VIEW_INFO_REGISTERED_AS_SMES(request):
    information=Register_as_smes.objects.all()
    context={
        "information":information
    }
    return render(request,"Manager/view_info_register_as_smes.html",context)


def MANAGER_VIEW_INFO_REGISTERED_AS_STARTUP(request):
    S_information = Register_as_startUp.objects.all()
    context = {
        "S_information": S_information
    }
    return render(request, "Manager/view_info_register_as_startUp.html", context)

