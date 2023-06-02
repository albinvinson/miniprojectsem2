from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method=='GET':
        return render(request,'registration.html')
    else:
        name=request.POST.get('name')
        phone=request.POST['phone']
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_date=UserDetail(uname=name,phone=phone,email=email,passwd=password)
        user_date.save()
        return render(request,'index.html')
    

def login(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user_check=UserDetail.objects.filter(email=uname,passwd=passwd)
        if len(user_check)==1:
            request.session['user_id'] = user_check[0].id
            request.session['user_name'] = user_check[0].uname
            context = {'uname': request.session['user_name']}
            return render(request,'home.html',context)
        else:
            return render(request,'index.html')
    else:
        return render(request,'login.html')
        


def booking(request):
        if request.method=='POST':
            user_id = request.session['user_id']
            userDetail = UserDetail.objects.get(pk=int(user_id))
            name=userDetail
            phone=request.POST.get('phone')
            gender=request.POST.get('gender')
            date=request.POST.get('date')
            time=request.POST.get('time')
            Booking.objects.create(user=name,phone=phone,gender=gender,date=date,appointment_time=time)
            context = {'uname': request.session['user_name']}
            return render(request,'home.html',context)
        else:
            return render(request,'booking.html')
   
    

def home(request):
    
        context = {'uname': request.session['user_name']}
        return render(request,'home.html',context)
   

def logout(request):
   
        del request.session['user_id']
        del request.session['user_name']
        return redirect('login')