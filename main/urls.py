from django.urls import path
from .views import HomeView,LoginView,LogoutView,EmployeeDetailView,AddEmployeeView,delete_employee,Scheduled,ScheduledDetailView,delete_scheduled,AddScheduledView,MessageDetailView,AddMessageView,delete_message,MessagesView,OutOfOrderView,AddOutOfOrderView,delete_out_of_order

urlpatterns = [

    path('',HomeView.as_view(),name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LoginView.as_view(),name='logout'),
    # Employeelar uchun urllar
    path('employee_detail/<int:pk>',EmployeeDetailView.as_view(),name='employee_detail'),
    path('delete_employee/<int:pk>',delete_employee,name='delete_employee'),
    path('add_employee/',AddEmployeeView.as_view(),name='add_employee'),

# Scheduled Messsage lar uchun urllar
    path('schuduled_messages/',Scheduled.as_view(),name='scheduled_messages'),
    path('scheduled_message_detail/<int:pk>',ScheduledDetailView.as_view(),name='scheduled_message_detail'),
    path('add_scheduled_messages/',AddScheduledView.as_view(),name='add_scheduled_messages'),
    path('delete_scheduled_message/<int:pk>',delete_scheduled,name='delete_schedulet'),

# Message templatelar uchun urllar
    path('messages/',MessagesView.as_view(),name='messages'),
    path('message_detail/<int:pk>',MessageDetailView.as_view(),name='message_detail'),
    path('add_messages/',AddMessageView.as_view(),name='add_messages'),
    path('delete_message/<int:pk>',delete_message,name='delete_message'),

# Navbatdan tashqari messagelar uchun
    path('out_of_order/',OutOfOrderView.as_view(),name='out_of_order'),
    path('add_out_of_order/',AddOutOfOrderView.as_view(),name='add_out_of_order'),
    path('delete_out_of_order/<int:pk>',delete_out_of_order,name='delete_out_of_order'),
]