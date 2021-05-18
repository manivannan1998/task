from django.shortcuts import render
from . import  models
from . models import student
from . models import mark
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def Index(request):
   return render(request, 'index.html',{})



def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def reg_done(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
      #  phone = request.POST['phone']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if password == repeat_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return render (request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return render (request, 'register.html')
            
            else:
                user = User.objects.create_user(username = username, email = email, password=password)
                user.save();
                print('user created')
               # return render (request, 'register.html')
        else:
            messages.info(request, 'password not matching...')
            return render (request, 'register.html')
        
        return render(request, 'reg_done.html')

    else:
        return render (request, 'register.html')

def log_done(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'log_done.html')

        else:
            return render(request, 'sorry.html')


    else:
        return render(request, 'sorry.html')


def student(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('rno') and request.POST.get('dob'):
            saverecord=student()
            saverecord.name=request.POST.get('name')
            saverecord.rno=request.POST.get('rno')
            saverecord.dob=request.POST.get('dob')
            saverecord.save()
            messages.success(request, 'Done Successfully...')
    return render (request, 'student.html')

def reply(request):
    #student_name =request.get["name"]
    markobj=mark.objects.all()
    #mark.objects.total().aggregate(Avg("Grade"))
    return render(request,'reply.html', {"mark":markobj})

def result(request):
    return render(request,'result.html')