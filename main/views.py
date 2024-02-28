from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Positions, Employees,Message_rass,Messages,Out_of_order
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.cache import cache
# Create your views here.

@login_required
def delete_employee(request,pk):
    try:
        resident = get_object_or_404(Employees,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        resident.delete() 
          
        return redirect('/')   



class HomeView(LoginRequiredMixin,View):

    def get(self, request):
        positions = Positions.objects.all()
        employees = Employees.objects.all()
        context = {"admin":request.user,"positions":positions,"employees":employees}
        return render(request,'index.html',context)
    
    def post(self,request):

        selected_option = request.POST.get('selected_option')
        positions = Positions.objects.all()
        position = Positions.objects.get(title=selected_option)
        employees = Employees.objects.filter(position=position)
        context = {"admin":request.user,"positions":positions,"employees":employees}

        return render(request,'index.html',context)

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self, request):
        print("posting login")
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return redirect('/login')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return redirect('/login')
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect( '/login')
    
class EmployeeDetailView(UpdateView):
    template_name = "update_employee.html"
    model = Employees
    fields = "__all__"
    success_url = "/"

class AddEmployeeView(CreateView):
    template_name = "update_employee.html"
    model = Employees
    fields = "__all__"
    success_url = "/"

# Employee uchun yozilgan viewlar tugadi
    
# ###################################################################################################################33

# Scheduled yani planlashtirilgan messagelar uchun yozilgan viewlar
import asyncio
from datetime import datetime
class Scheduled(LoginRequiredMixin,View):

    def get(self, request):
        scheduled_messages = Message_rass.objects.all()
        context = {"admin":request.user,"scheduled":scheduled_messages}
        return render(request,'scheduled_messages.html',context)
    
    def post(self,request):
        return render(request,'scheduled_messages.html')

class ScheduledDetailView(UpdateView):
    template_name = "update_employee.html"
    model = Message_rass
    fields = "__all__"
    success_url = "/schuduled_messages/"

class AddScheduledView(CreateView):
    template_name = "update_employee.html"
    model = Message_rass
    fields = "__all__"
    success_url = "/schuduled_messages/"


def delete_scheduled(request,pk):
    try:
        sche_messages = get_object_or_404(Message_rass,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        sche_messages.delete() 
          
        return redirect('/schuduled_messages/')   

# Scheduled uchun yozilgan viewlar tugadi
    
# ###################################################################################################################33

# Message templatelar  uchun yozilgan viewlar
    
class MessagesView(LoginRequiredMixin,View):

    def get(self, request):
        messages = Messages.objects.all()
        
        context = {"admin":request.user,"messages":messages}

        return render(request,'message_templates.html',context)
    
    def post(self,request):

        selected_option = request.POST.get('selected_option')
        positions = Positions.objects.all()
        position = Positions.objects.get(title=selected_option)
        employees = Employees.objects.filter(position=position)
        
        context = {"admin":request.user,"positions":positions,"employees":employees}

        return render(request,'message_templates.html',context)

class MessageDetailView(UpdateView):
    template_name = "update_employee.html"
    model = Messages
    fields = "__all__"
    success_url = "/messages/"

class AddMessageView(CreateView):
    template_name = "update_employee.html"
    model = Messages
    fields = "__all__"
    success_url = "/messages/"


def delete_message(request,pk):
    try:
        sche_messages = get_object_or_404(Messages,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        sche_messages.delete() 
          
        return redirect('/messages/')   

# Message templatelar uchun yozilgan viewlar tugadi   
    
# ###################################################################################################################33

# Out of orderlar  uchun yozilgan viewlar
def out_of_order_cache_get():
    out_of_order_base = Out_of_order.objects.all()
    out_of_order_cache = cache.get('out_of_order_cache')
    if not out_of_order_cache or out_of_order_cache != out_of_order_base:
        out_of_order_cache = list(Out_of_order.objects.all())
        cache.set('out_of_order_cache', out_of_order_cache)
    return out_of_order_cache
class OutOfOrderView(LoginRequiredMixin,View):

    def get(self, request):
        messages = Out_of_order.objects.all()
        out_of_order_cache = cache.get('out_of_order_cache')
        for message in messages:

            print(message.get_employees()) 
        context = {"admin":request.user,"messages":messages}

        return render(request,'out_of_order.html',context)
    
    def post(self,request):
        return render(request,'out_of_order.html')

from .utils import message_sender
from .forms import Out_of_order_form
class AddOutOfOrderView(View):
    def get(self, request):
        form = Out_of_order_form
        context = {"form":form}
        return render(request,'update_employee.html',context)
    def post(self, request):
        form = Out_of_order_form(request.POST)
        if form.is_valid():
            employees = form.cleaned_data["employee"]
            positions = form.cleaned_data["position"]
            templates = form.cleaned_data["template"]
            messages = form.cleaned_data["message"]
            employees_list = []
            for employee in employees:
                employees_list.append(employee.telegram)
            for position in positions:
                employee_from_position = Employees.objects.filter(position=position)
                for emp in employee_from_position:
                    if emp.telegram not in employees_list:
                        employees_list.append(emp.telegram)
            if templates:
                template_message = f"{templates.info} \n {messages}"
            else:
                template_message = messages
        for chat_id in employees_list:
            message_sender(chat_id=chat_id,text=template_message)
            # asyncio.run(messega_sender(chat_id=chat_id,message=template_message))
            
            form.save()
        return redirect('/out_of_order/')
    


def delete_out_of_order(request,pk):
    try:
        messages = get_object_or_404(Out_of_order,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        messages.delete() 
          
        return redirect('/out_of_order/')   
