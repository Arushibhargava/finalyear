from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Signup
from django.contrib import messages
def main(request):
    return render(request, 'mentor/main.html')



def cdashboard(request):
    return render(request, 'mentor/cdashboard.html')

def clogin(request):
    return render(request, 'mentor/clogin.html')

def cnotification(request):
    return render(request, 'mentor/cnotification.html')

def cproposals(request):
    return render(request, 'mentor/cproposals.html')
def creport(request):
    return render(request, 'mentor/creport.html')

def ctasks(request):
    return render(request, 'mentor/ctasks.html')
def dashboard(request):
    return render(request, 'mentor/dashboard.html')
def login(request):
    return render(request, 'mentor/login.html')

def Mlogin(request):
    return render(request, 'mentor/Mlogin.html')

def Mproject(request):
    return render(request, 'mentor/Mproject.html')

def notification(request):
    return render(request, 'mentor/notification.html')

def report(request):
    return render(request, 'mentor/report.html')

def signup(request):
    return render(request, 'mentor/signup.html')

def tasks(request):
    return render(request, 'mentor/tasks.html')

def tdashboard(request):
    return render(request, 'mentor/tdashboard.html')

def tgroups(request):
    return render(request, 'mentor/tgroups.html')

def tlogin(request):
    return render(request, 'mentor/tlogin.html')

def tnotification(request):
    return render(request, 'mentor/tnotification.html')

def tproject(request):
    return render(request, 'mentor/tproject.html')

def treport(request):
    return render(request, 'mentor/treport.html')

def tsignup(request):
    return render(request, 'mentor/tsignup.html')

def ttasks(request):
    return render(request, 'mentor/ttasks.html')






def insertmentor(request):
    vuname=request.POST['tuname']
    vuemail=request.POST['tuemail']
    vucontact=request.POST['tucontact']
    vupassword=request.POST['tupassword']
    us=Signup(uname=vuname,uemail=vuemail,ucontact=vucontact,upassword=vupassword)
    us.save()
    return render(request, 'Mentor_frontend/login.html',{})