'''from django.conf.urls import urls
from employeeapi import views

urlpatterns = [
    urls(r'^employee$',views.employeeApi),
    urls(r'^employee$/([0-9]+$')
]
from django.conf.urls import url
from employeeapi import views

urlpatterns = [
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi)
]'''
from django.urls import re_path
from employeeapi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # registration
    re_path(r'^employee$', views.employeeApi, name='employee-list'),
    re_path(r'^employee/(?P<id>[0-9]+)$', views.employeeApi, name='employee-detail'),
    
    # adding urls for the task management
    re_path('task/', views.taskApi, name='task-list'),
    re_path('task/<int:id>/', views.taskApi, name='task-detail'),
    
    # adding urls for the attendance
    
    re_path(r'^attendance/$', views.attendanceApi, name='attendance-list'),
    re_path(r'^attendance/(?P<id>[0-9]+)$', views.attendanceApi, name='attendance-detail'),


    re_path(r'^atten/$', views.attenApi, name='atten-list'),
    re_path(r'^atten/(?P<id>[0-9]+)$', views.attenApi, name='atten-detail'),

   
# URLs for the MarkManualAttendance API
    re_path(r'^markmanualattendance/$', views.mark_manual_attendance_api, name='markmanualattendance-list'),
    re_path(r'^markmanualattendance/(?P<id>[0-9]+)$', views.mark_manual_attendance_api, name='markmanualattendance-detail'),

# URLs for the LeavelAttendance API

    re_path(r'^leaveattendance/$', views.leave_attendance_api, name='leave-application-list'),
    re_path(r'^leaveattendance/(?P<ID>[0-9]+)$', views.leave_attendance_api, name='leave-application-detail'),
    
    
# url for the VisitShop API

    re_path(r'^visitshop/$', views.visit_api, name='visit-list-create'),

    re_path(r'^visitshop/(?P<ID>[0-9]+)$', views.visit_api, name='visit-detail'),
    
#url for invoice API

    re_path(r'^orderinvoices/$', views.order_invoice_api, name='orderinvoice-list-create'),
    re_path(r'^orderinvoices/(?P<ID>[0-9]+)$', views.order_invoice_api, name='orderinvoice-detail'),
    
    
    re_path(r'^expenses/$', views.expense_api, name='expense-list-create'),
    re_path(r'^expenses/(?P<ID>[0-9]+)$', views.expense_api, name='expense-detail'),

    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    


