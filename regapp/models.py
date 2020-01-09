from django.db import models
# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=20)
    mobilenumber = models.IntegerField()
    password = models.CharField(max_length=20)
   

    class meta:
        db_name = 'Person'

class Admin(models.Model):
    name     = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    class meta:
        db_table = "Admin"
class Faculty(models.Model):
    Fname  = models.CharField(max_length=20)
    Fid =models.IntegerField()
    Address=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Qual=models.CharField(max_length=20)
    Mobileno=models.IntegerField()
    Batch=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    password=models.CharField(max_length=10,default="")

    
    class meta:
        db_table = "Faculty" 


class Student(models.Model):
    Sname=models.CharField(max_length=20)
    Sid=models.IntegerField(default="",null="True",blank="True")
    Address=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    AdmDate=models.DateField()
    Mobileno=models.IntegerField()
    Batch=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Guardian=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    
    class meta:
        db_table="Student"
class Attend(models.Model):
    Sname=models.CharField(max_length=20)
    Sid=models.IntegerField()
    Period1=models.CharField(max_length=20)
    Period2=models.CharField(max_length=20)
    Period3=models.CharField(max_length=20)
    Period4=models.CharField(max_length=20)

    class meta:
        db_table="Attend"

class Mark(models.Model):
    Sname=models.CharField(max_length=20)
    Sid=models.IntegerField(null="True",blank="True")
    C=models.IntegerField()
    CPP=models.IntegerField()
    Java=models.IntegerField()
    Python=models.IntegerField()
    Html=models.IntegerField()

    class meta:
        db_table="Mark"

class Leave_s(models.Model):
    Sname=models.CharField(max_length=20)
    Sid=models.IntegerField()
    From_date=models.DateField()
    To_date=models.DateField()
    Reason=models.CharField(max_length=200)
    Status=models.CharField(max_length=20,default="" ,null="True",blank="True")

    class meta:
        db_table="Leave_s"

class leave_f(models.Model):
    Fname=models.CharField(max_length=20,default="")
    Fid=models.IntegerField()
    From_date=models.DateField()
    To_date=models.DateField()
    Reason=models.CharField(max_length=200)
    Status=models.CharField(max_length=20,default="",null="True",blank="True")

    class meta:
        db_table="leave_f"