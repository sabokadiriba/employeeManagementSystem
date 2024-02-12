
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views,Manager_views,Employee_views,Staff_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #reset password path
    path('',include('app.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),



    path('', views.DASHBOARD, name='dashboard'),
    path('base',views.BASE , name='base'),
    path('message', views.MESSAGE, name='message'),
    path('help', views.HELP, name='help'),



    #login path
    path('login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # profile path
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),
    #Manager path
    path('Manager/home', Manager_views.MANAGER_HOME, name='manager_home'),
    path('Manager/Add/Employee', Manager_views.ADD_EMPLOYEE, name='add_employee'),
    path('Manager/View/Employee', Manager_views.VIEW_EMPLOYEE, name='view_employee'),
    path('Manager/Update/Employee_info/<str:id>', Manager_views.MANAGER_UPDATE_EMPLOYEE_INFO, name='manager_update_employee_info'),
    path('Manager/Save/Employee_info', Manager_views.MANAGER_SAVE_EMPLOYEE_INFO,name='manager_save_employee_info'),
    path('Manager/Delete/Employee/<str:admin>', Manager_views.MANAGER_DELETE_EMPLOYEE,name='manager_delete_employee'),

    path('Manager/Add/Staff', Manager_views.ADD_STAFF, name='add_staff'),
    path('Manager/View/Staff', Manager_views.VIEW_STAFF, name='view_staff'),
    path('Manager/Update/Staff_info/<str:id>', Manager_views.MANAGER_UPDATE_STAFF_INFO,name='manager_update_staff_info'),
    path('Manager/Save/Save_info', Manager_views.MANAGER_SAVE_STAFF_INFO,name='manager_save_staff_info'),
    path('Manager/Delete/Staff/<str:admin>', Manager_views.MANAGER_DELETE_STAFF,name='manager_delete_staff'),

    path('Manager/Add/Session',Manager_views.ADD_SESSION, name='add_session'),
    path('Manager/View/Session',Manager_views.VIEW_SESSION, name='view_session'),
    path('Manager/Update/Session/<str:id>', Manager_views.MANAGER_UPDATE_SESSION,name='manager_update_session'),
    path('Manager/Save/Session', Manager_views.MANAGER_SAVE_SESSION, name='manager_save_session'),
    path('Manager/Delete/Session/<str:id>', Manager_views.MANAGER_DELETE_SESSION,name='manager_delete_session'),



    path('Manager/Add/Department', Manager_views.ADD_DEPARTMENT, name='add_department'),
    path('Manager/View/Department', Manager_views.VIEW_DEPARTMENT, name='view_department'),
    path('Manager/Update/Department/<str:id>', Manager_views.MANAGER_UPDATE_DEPARTMENT,name='manager_update_department'),
    path('Manager/Save/Department', Manager_views.MANAGER_SAVE_DEPARTMENT, name='manager_save_department'),
    path('Manager/Delete/Department/<str:id>', Manager_views.MANAGER_DELETE_DEPARTMENT,name='manager_delete_department'),

    path('Manager/View/Employee_leave', Manager_views.VIEW_EMPLOYEE_LEAVE, name='view_employee_leave'),
    path('Manager/Approve/Employee_leave/<str:id>', Manager_views.APPROVE_EMPLOYEE_LEAVE, name='approve_employee_leave'),
    path('Manager/Dispprove/Employee_leave/<str:id>', Manager_views.DISAPPROVE_EMPLOYEE_LEAVE, name='disapprove_employee_leave'),


    path('Manager/Send/Notification/To/Employee', Manager_views.SEND_NOTIFICATION_TO_EMPLOYEE, name='send_notification_to_employee'),
    path('Manager/Save/Notification/Of/Employee', Manager_views.SAVE_NOTIFICATION_OF_EMPLOYEE,name='save_notification_of_employee'),

    path('Manager/Send/Notification/To/Staff', Manager_views.SEND_NOTIFICATION_TO_STAFF,name='send_notification_to_staff'),
    path('Manager/Save/Notification/Of/Staff', Manager_views.SAVE_NOTIFICATION_OF_STAFF,name='save_notification_of_staff'),

    path('Manager/Reply_feedback', Manager_views.REPLY_EMPLOYEE_FEEDBACK, name='manager_reply_employee_feedback'),
    path('Manager/Save/feedback', Manager_views.SAVE_EMPLOYEE_FEEDBACK_REPLY, name='manager_save_employee_feedback'),

    path('Manager/Reply_staff_feedback', Manager_views.REPLY_STAFF_FEEDBACK,name='manager_reply_staff_feedback'),
    path('Manager/Save/Staff/feedback', Manager_views.SAVE_STAFF_FEEDBACK_REPLY, name='manager_save_staff_feedback'),

    path('Manager/View_attendance', Manager_views.MANAGER_VIEW_ATTENDANCE, name='manager_view_attendance'),
    path('Manager/View_onfo_registered_as_smes', Manager_views.MANAGER_VIEW_INFO_REGISTERED_AS_SMES,name='manager_view_onfo_registered_as_smes'),
    path('Manager/View_onfo_registered_as_startUp', Manager_views.MANAGER_VIEW_INFO_REGISTERED_AS_STARTUP,name='manager_view_onfo_registered_as_startUp'),

                  #HRM path
    path('HRM/home', Staff_views.STAFF_HOME, name='staff_home'),
    path('HRM/Take_attendance', Staff_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('HRM/Save_attendance', Staff_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('HRM/view_attendance', Staff_views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

    path('HRM/View_notification', Staff_views.STAFF_VIEW_NOTIFICATION, name='staff_view_notification'),
    path('HRM/mark_as_read_notification/<str:status>',Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_mark_as_read_notification'),

    path('HRM/feedback', Staff_views.STAFF_FEEDBACK, name='staff_feedback'),
    path('HRM/Save/feedback', Staff_views.SAVE_STAFF_FEEDBACK, name='save_staff_feedback'),

                  # Employee path
    path('Employee/home',Employee_views.EMPLOYEE_HOME,name='employee_home'),
    path('Employee/applay_leave', Employee_views.EMPLOYEE_APPLAY_LEAVE, name='employee_applay_leave'),
    path('Employee/Applay_leave_save', Employee_views.EMPLOYEE_APPLAY_LEAVE_SAVE, name='employee_applay_leave_save'),

    path('Employee/View_notification', Employee_views.VIEW_NOTIFICATION,name='view_notification'),
    path('Employee/mark_as_read_notification/<str:status>', Employee_views.EMPLOYEE_NOTIFICATION_MARK_AS_DONE,name='employee_mark_as_read_notification'),

    path('Employee/feedback',Employee_views.EMPLOYEE_FEEDBACK, name='employee_feedback'),
    path('Employee/Save/feedback', Employee_views.SAVE_EMPLOYEE_FEEDBACK, name='save_employee_feedback'),

    path('Employee/view_attendance', Employee_views.EMPLOYEE_VIEW_ATTENDANCE, name='employee_view_attendance'),

    path('Register/As_smes', views. REGISTER_AS_SMES, name='register_as_smes'),
    path('Save/Register/As_smes', views.SAVE_REGISTER_AS_SMES, name='save_register_as_smes'),
    path('Register/As_StarUp', views. REGISTER_AS_STARTUP, name='register_as_startUp'),
    path('Save/Register/As_StarUp', views.SAVE_REGISTER_AS_STARTUP, name='save_register_as_startUp'),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
