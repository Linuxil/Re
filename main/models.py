from django.db import models

class Day(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday ', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=20, choices=DAY_CHOICES)

    def __str__(self) -> str:
        return self.day_of_week
    

class Positions(models.Model):
    title = models.CharField(max_length=256, unique=True)
    def __str__(self) -> str:
        return self.title

class Employees(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    telegram = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name
    
    

class Messages(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self) -> str:
        return self.title

class Message_rass(models.Model):
    employee = models.ManyToManyField(Employees, blank=True)
    template = models.ForeignKey(Messages,on_delete=models.CASCADE,null=True, blank=True)
    position = models.ManyToManyField(Positions, blank=True)
    day_of_week = models.ManyToManyField(Day,blank=True)
    time = models.CharField(max_length=5)
    class Meta:
        verbose_name_plural = "Schedule_messages"

    def __str__(self) -> str:
        return f"{self.position} {self.day_of_week} {self.template}"
    def get_employees(self):
        employees = self.employee.all()
        employee_name = []
        for employee in employees:
            employee_name.append(employee.name)
        return employee_name

    def get_positions(self):
        positions = self.position.all()
        position_title = []
        for position in positions:
            position_title.append(position.title)
        return position_title

    def get_day_of_week(self):
        days = self.day_of_week.all()
        days_title = []
        for day in days:
            days_title.append(day.day_of_week)
        return days_title




class Out_of_order(models.Model):
    employee = models.ManyToManyField(Employees, blank=True)
    template = models.ForeignKey(Messages,on_delete=models.CASCADE,null=True, blank=True)
    message = models.TextField()
    position = models.ManyToManyField(Positions, blank=True)
    def get_employees(self):
        employees = self.employee.all()
        employee_name = []
        for employee in employees:
            employee_name.append(employee.name)
        return employee_name

    def get_positions(self):
        positions = self.position.all()
        position_title = []
        for position in positions:
            position_title.append(position.title) 
        return position_title
