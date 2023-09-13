from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse  
from functions.function import handle_uploaded_file  
from accounts.forms import FileForm
     
@login_required
def home_view(request):
    if request.method == 'POST':  
            student = FileForm(request.POST, request.FILES)
            if student.is_valid():  
                print(request.FILES['file'])
                handle_uploaded_file(request.FILES['file'])  
                return render(request,"accounts/success.html",{})  
            else:  
               student = FileForm()  
    student=FileForm     
    return render(request,"accounts/home.html",{'form':student})

def login_view(request):
    form=AuthenticationForm(request,data=request.POST)
    
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
             user=form.get_user()
             login(request,user)
             return redirect('/home')
    else:
        form=AuthenticationForm(request)
    context={"form":form}        

    return render(request,'accounts/login.html',context=context)

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect("/login")

    return render(request,'accounts/logout.html',{})


# def register_view(request):
#     form=UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj=form.save()
#         return redirect("/login")
#     context={"form":form}
#     return render(request,'accounts/register.html',context=context)