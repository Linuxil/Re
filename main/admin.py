from django.contrib import admin
from .models import Positions, Employees, Messages, Message_rass,Day,Out_of_order
# Register your models here.

admin.site.register(Positions)
admin.site.register(Employees)
admin.site.register(Messages)
admin.site.register(Message_rass)
admin.site.register(Day)
admin.site.register(Out_of_order)
 