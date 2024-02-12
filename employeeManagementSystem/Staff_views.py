from django.shortcuts import render,redirect,HttpResponse
from app.models import CustomUser,Session_year,Department,Employee,Attendance,Attendance_report,Staff,Staff_notification,Staff_feedback
from django.contrib import messages



def STAFF_HOME(request):
    return render(request,'HRM/staff_home.html')


def STAFF_TAKE_ATTENDANCE(request):
    department=Department.objects.all()
    session_year= Session_year.objects.all()
    action=request.GET.get('action')
    get_department=None
    get_session_year=None
    employee=None

    if action is not None:
        if request.method == "POST":
            department_id=request.POST.get('department_id')
            session_year_id = request.POST.get('session_year_id')

            get_department= Department.objects.get(id=department_id)
            get_session_year=Session_year.objects.get(id=session_year_id)
            employee = Employee.objects.filter(department_id=department_id)

    dic={
        'department':department,
        'session_year':session_year,
        'get_department':get_department,
        'get_session_year':get_session_year,
        'action':action,
        'employee':employee,
    }
    return render(request, 'HRM/take_attendance.html',dic)




def STAFF_SAVE_ATTENDANCE(request):
    department_id= request.POST.get('department_id')
    session_year_id= request.POST.get('session_year_id')
    attendance_date = request.POST.get('attendance_date')
    employee_id = request.POST.getlist('employee_id')

    department=Department.objects.get(id=department_id)
    session_year=Session_year.objects.get(id=session_year_id)
    attendance=Attendance(
        department_id=department,
        attendance_data=attendance_date,
        session_year_id=session_year,

    )
    attendance.save()

    for i in employee_id:
        e_id=int(i)
        attende_employee=Employee.objects.get(id=e_id)
        attendance_report=Attendance_report(
            employee_id=attende_employee,
            attendance_id=attendance

        )
        attendance_report.save()

    messages.success(request, ' attendance is recorded')
    return  redirect('staff_take_attendance')


def STAFF_VIEW_ATTENDANCE(request):
    session_year=Session_year.objects.all()
    department=Department.objects.all()
    action=request.GET.get('action')

    get_department = None
    get_session_year = None
    attendance_report=None
    attendance_date=None

    if action is not None:
        if request.method == "POST":
            department_id = request.POST.get('department_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_department = Department.objects.get(id=department_id)
            get_session_year = Session_year.objects.get(id=session_year_id)

            attendance=Attendance.objects.filter(department_id=get_department,attendance_data=attendance_date)
            for i in attendance:
                attendance_id=i.id
                attendance_report=Attendance_report.objects.filter(attendance_id=attendance_id)


    context={
        'department':department,
        'session_year':session_year,
        'action':action,
        'get_department':get_department,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,



    }
    return render(request,'HRM/view_attendance.html',context)


def STAFF_VIEW_NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id
        notification = Staff_notification.objects.filter(staff_id=staff_id)
        context = {
            'notification': notification,
        }
    return render(request, 'HRM/view_notification.html', context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('view_notification')


def STAFF_FEEDBACK(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id
        feedback_history = Staff_feedback.objects.filter(staff_id=staff_id)
        context = {
            'feedback_history': feedback_history,
        }
        return render(request, 'HRM/feedback.html', context)


def SAVE_STAFF_FEEDBACK(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin=request.user.id)

        see_feedback = Staff_feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_replay="",
        )
        see_feedback.save()
        messages.success(request, 'feedback is sent successfully')
        return redirect('staff_feedback')
