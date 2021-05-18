from django.db import models
from datetime import date
# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    #phone = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    repeat_password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class student(models.Model):
    name=models.CharField(max_length=30)
    rno=models.IntegerField(primary_key=True, unique=True)
    dob=models.DateField(null=True,blank=True)
    displayFiels =['name', 'rno', 'dob']
    class Meta:
        db_table:"student"
        
class mark(models.Model):
    sname=models.CharField(max_length=30)
    srno=models.IntegerField(primary_key=True)
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    total=models.IntegerField()
    class Meta:
        db_table:"mark"