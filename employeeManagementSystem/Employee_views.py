from django.shortcuts import render,redirect,HttpResponse
from app.models import CustomUser,Session_year,Department,Employee,Employee_leave,Employee_notification,Employee_feedback,Attendance_report
from django.contrib import messages

def EMPLOYEE_HOME(request):
    return render(request,'Employee/employee_home.html')




def EMPLOYEE_APPLAY_LEAVE(request):
    employee = Employee.objects.filter(admin = request.user.id)
    for i in employee:
        employee_id = i.id
        leave_employee_history = Employee_leave.objects.filter(employee_id=employee_id)
        context = {
            'leave_employee_history': leave_employee_history,
        }

    return render(request, 'Employee/applay_leave.html', context)



def EMPLOYEE_APPLAY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Employee.objects.get(admin=request.user.id)
        print(staff)

        leave = Employee_leave(
            employee_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave.save()
        messages.success(request, 'notification is sent successfully')
    return redirect('employee_applay_leave')


def VIEW_NOTIFICATION(request):
    employee = Employee.objects.filter(admin=request.user.id)

    for i in employee:
        employee_id = i.id
        notification = Employee_notification.objects.filter(employee_id=employee_id)
        context = {
            'notification': notification,
        }
    return render(request,'Employee/view_notification.html',context)



def EMPLOYEE_NOTIFICATION_MARK_AS_DONE(request,status):
    notification=Employee_notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('view_notification')


def EMPLOYEE_FEEDBACK(request):
    employee = Employee.objects.filter(admin=request.user.id)

    for i in employee:
        employee_id = i.id
        feedback_history = Employee_feedback.objects.filter(employee_id=employee_id)
        context = {
            'feedback_history': feedback_history,
        }
        return render(request, 'Employee/feedback.html', context)


def SAVE_EMPLOYEE_FEEDBACK(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        employee = Employee.objects.get(admin=request.user.id)

        see_feedback = Employee_feedback(
            employee_id=employee,
            feedback=feedback,
            feedback_replay="",
        )
        see_feedback.save()
        messages.success(request, 'feedback is sent successfully')
        return redirect('employee_feedback')


def EMPLOYEE_VIEW_ATTENDANCE(request):
    employee=Employee.objects.get(admin=request.user.id)
    attendance_report=Attendance_report.objects.filter(employee_id=employee)
    context={
        'attendance_report':attendance_report,
    }
    return render(request,'Employee/view_attendance.html',context)