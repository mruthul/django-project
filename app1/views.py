from django.contrib import messages
from django.shortcuts import redirect, render
from app1.forms import Changepassword, Editform, Loginform
from django.contrib.auth import logout as logouts
from app1.models import Image, Signup

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        tab=Signup(Name=name,Age=age,Password=password,Email=email)
        tab.save()
    return render(request,'signup.html')     

def login(request):
    if request.method=='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Signup.objects.filter(Email=email).exists()
            if not user:
                messages.warning(request,"user not exist")
                return redirect('/login')
            elif password != user.Password:
                messages.warning(request,"No match")
            else:
                messages.success(request,'login successfull')
                return redirect('/home/%s' % user.id)
    else:
        form=Loginform()
    return render(request,'login.html',{'form':form})
    
def home(request,id):
    data=Signup.objects.get(id=id)
    return render(request,'home.html',{'data':data})    

def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=Editform(request.POST or None,instance=user)
        if form.is_valid():
            name=form.cleaned_data['Name']
            email=form.cleaned_data['Email']
            messages.success(request,'update successfull')
            form.save()
            return redirect('/home/%s' % user.id)
    else:
        form=Editform(instance=user)
        return render(request,'update.html',{'form':form,'user':user})

def changepassword(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=Changepassword(request.POST or None)
        if form.is_valid():
            opassword=form.cleaned_data['Old_Password'] 
            npassword=form.cleaned_data['New_Password']
            cpassword=form.cleaned_data['Confirm_Password']
            if opassword != user.Password:
                messages.warning(request,'incorrect password')
                return redirect('/home/%s' % user.id)
            elif npassword==opassword:
                messages.warning(request,'same password')
                return redirect('/home/%s' % user.id)
            elif npassword != cpassword:
                messages.warning(request,'password not same')
                return redirect('/home/%s' % user.id)    
            else: 
                user.Password=npassword
                user.save()       
                messages.success(request,'Password Changed')
                return redirect('/login')
    else:
        form=Changepassword()     
    return render(request,'changepsw.html',{'form':form,'user':user})          

def logout(request):
    logouts(request)
    messages.success(request,'successfully logedout')
    return redirect('/')
    
def gallery(request):
    data=Image.objects.all()
    return render(request,'gallery.html',{'data':data})
     

def details(request,id):
    data=Image.objects.get(id=id)
    return render(request,'details.html',{'data':data})      
   
