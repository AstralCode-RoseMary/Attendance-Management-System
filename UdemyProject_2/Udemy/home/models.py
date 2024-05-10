
from django.db import models
from django.urls import reverse


# Create your models here.

class Register(models.Model):
    register_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    per_address = models.CharField(max_length=100)
    cur_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(default="no-reply@example.com")
    dob = models.DateField()
    department = models.CharField(max_length=20)
    seating_location = models.CharField(max_length=20)
    date_of_join = models.DateField()
    date_of_confirmation = models.DateField()
    employee_status = models.CharField(max_length=10)
    work_phone = models.CharField(max_length=10)
    experience = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Login(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Timeslot(models.Model):
    time_id = models.AutoField(primary_key=True)
    cdate = models.DateField( )
    checkin = models.TimeField()
    checkout = models.TimeField()

class Department(models.Model):
    dept_id = models.IntegerField(auto_created=True, primary_key=True)
    dept_name = models.CharField()
    dept_dis = models.CharField()
    dept_parent = models.IntegerField(null=True)
    dept_level = models.IntegerField()
    create_on = models.DateField()
    create_by = models.CharField()

class Leaveform(models.Model):
    leave_form_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    lead = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=100)
    reason = models.TextField(max_length=250)

class Profile(models.Model):
    username = models.CharField(max_length=100)
    dob = models.DateField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_d = models.DateField()
    goalname = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)






