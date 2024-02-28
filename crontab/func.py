import telebot
from main.models import Message_rass,Employees,Messages,Positions
from datetime import datetime, timedelta
from main.utils import message_sender

bot = telebot.TeleBot(token='6731382749:AAF_Ur17TbHc8Vs8s7KMEhGJhlR_8GrH0BI')

def counter():
    messages = Message_rass.objects.select_related('template')
    today = datetime.today().strftime('%A')
    time_now = datetime.now().strftime('%H:%M')
    scheduled_messages = Message_rass.objects.all()
    for schedule in scheduled_messages:
        if today in schedule.get_day_of_week() and schedule.time == time_now:
            print('salom')
            employees_list = []
            employees = schedule.get_employees()
            positions = schedule.get_positions()
            for employee in employees:
                emp_em = Employees.objects.get(name=employee)
                employees_list.append(emp_em.telegram)
            for position in positions:
                position_emp = Employees.objects.filter(position=Positions.objects.get(title=position))
                for pos_emp in position_emp:
                    if pos_emp.telegram not in employees_list:
                        employees_list.append(pos_emp.telegram)
            message = schedule.template
            message_info = Messages.objects.get(title=message)
            for emp in employees_list:
                message_sender(emp, message_info.info)




