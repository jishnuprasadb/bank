from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from bank_app.models import Bank


# Create your views
def Home(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request, 'invalid credentiels')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not matching')
            return redirect('signup')

    return render(request,'signup.html')

def new_page(request):
    return render(request,'new_page.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        date_birth=request.POST['date']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        district=request.POST['district']
        branch=request.POST['branch']
        account=request.POST['account']
        materials=request.POST['material']
        bank=Bank(name=name,date_birth=date_birth,age=age,gender=gender,
                  phone=phone,email=email,address=address,district=district,
                  branch=branch,account_type=account,materials=materials)
        bank.save()
        messages.info(request,"Registration succesful")
    return render(request,'register.html')