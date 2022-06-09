from django.shortcuts import render
from login.models import *
# Create your views here.

def home(request):
    return render(request,template_name='home.html')

def signup(request):
    if request.method == 'POST':
        formdata = request.POST
        name = formdata.get('name')
        mail = formdata.get('mail')
        password = formdata.get('password')
        user = None
        if mail == '' or name == '' or password =='':
            if mail == '':
                message = "Email ID Can't be Blank..."
                return render(request, 'user_signup.html', {"message": message})
            elif name == '':
                message = "Name Can't be Blank..."
                return render(request, 'user_signup.html', {"message": message})
            else:
                message = "Password Can't be Blank..."
                return render(request, 'user_signup.html', {"message": message})
        if mail:
            user = User_signup.objects.filter(mail=mail).first()
        if user:
            user.name = formdata['name']
            message = 'Email ID is Already Register'
            return render(request, 'user_signup.html', {"message": message})
        else:
            user = User_signup(name=formdata['name'],
                                mail=formdata['mail'],
                                password=formdata['password'])
            message = 'User Added Successfully'
            user.save()
            return render(request,'user_signup.html',{"message":message})
    return render(request, 'user_signup.html', {"message": ''})

def login(request):
    if request.method == 'POST':
        formdata = request.POST
        mail = formdata.get('mail')
        password = formdata.get('password')
        if mail and password:
            username = User_signup.objects.filter(mail=mail,password=password).first()
            if username:
                return render(request,'book.html')
            else:
                message = 'Invalid Username or Password'
                return render(request,'login.html',{"message":message})
    return render(request, 'login.html')
