from django.shortcuts import render,redirect

from my_app.forms import Userregistrationform,Loginform,Taskform,ForgotpasswordForm,OtpverifyForm,ResetPasswordForm

from django.views.generic import View

from my_app.models import User,TaskModel,Otpmodel

from django.contrib.auth import authenticate,login,logout


from django.core.mail import send_mail

from django.utils.decorators import method_decorator


import random 


# ivai nqrr eyxt mdqm

# Create your views here.

# registration, login, task,add task, read task, delete tak,update,logout,forgot pswd



def is_user(fn):  # def get(request, **kwargs)
    def wrapper(request,**kwargs):
        id = kwargs.get("pk")  #{"pk": 2}

        item = TaskModel.objects.get(id = id) #taskmodel obj1

        if item.user_id == request.user:
            return fn(request,**kwargs)
        
        return redirect("login")
    
    return wrapper




class Userregisterview(View):

    def get(self,request):

        form = Userregistrationform

        return render(request,'signup.html',{"form":form})

    def post(self,request):

        form = Userregistrationform(request.POST) # which serves the data f

        if form.is_valid():

            print(form.cleaned_data) #dict

            username = form.cleaned_data.get('username')

            password =  form.cleaned_data.get('password')

            email = form.cleaned_data.get('email')

            User.objects.create_user(username=username,password=password,email=email)
        
        #return render(request,"signup.html",{"form":form})
        return redirect("login")
    

# Loginview
# 
# get,post


class Loginview(View):

    def get(self,request):

        form = Loginform()

        return render(request,"login.html",{"form":form})
    

    def post(self,request):

        form = Loginform(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user_obj = authenticate(request,username=username,password=password)
            if user_obj:

                login(request,user_obj)
                
            return redirect("task_list")
        else:

            form=Loginform()

            return render(request,"login.html",{"form":form,"error": "Invalid credentials"})

    
class Logoutview(View):
    def get(self,request):
        logout(request)

        return redirect("login")     

class addtaskview(View):
    def get(self,request):
        form = Taskform()

        return render(request,"addtask.html",{"form":form})  
    

    def post(self,request):
        form = Taskform(request.POST)

        if form.is_valid():
            TaskModel.objects.create(user_id=request.user, **form.cleaned_data)
            return redirect("task_list")   
        return render(request,"addtask.html",{"form":form})


class Taskreadview(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect("login")
        items = TaskModel.objects.filter(user_id=request.user)

        return render(request,"tasklist.html",{"items":items})
    


@method_decorator(decorator=is_user,name="dispatch")
class Taskupdateview(View):
    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        item = TaskModel.objects.get(id=id)
        form = Taskform(instance = item) 
        return render(request,"update.html",{"form":form})   
    
    def post(self,request,**kwargs):
        
        id = kwargs.get('pk')
        item = TaskModel.objects.get(id=id)

        form = Taskform(request.POST,instance=item)

        if form.is_valid():
            form.save()

            return redirect("task_list")
        return render(request,"update.html",{"form":form})    

@method_decorator(decorator=is_user,name="dispatch")
class Taskdeleteview(View):

    def get(self,request,**kwargs):
        id = kwargs.get("pk")

        TaskModel.objects.get(id=id).delete()

        return redirect("task_list")
    
@method_decorator(decorator=is_user,name="dispatch")
class Taskdetailview(View):
    def get(self,request,**kwargs):

        id = kwargs.get("pk")
        items = TaskModel.objects.get(id=id)  

        return render(request,"detail.html",{"items":items})  
    

class Taskedit(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk") 

        data = TaskModel.objects.get(id=id)

        data.completed_status = True
        data.save()

        return redirect("task_list")   
    

class Forgotpasswordview(View):

  def get(self,request):
    form = ForgotpasswordForm
    return render(request,"forgotpswd.html",{"form":form})
   
  def post(self,request):
      form = ForgotpasswordForm(request.POST)

      if form.is_valid():
          email = form.cleaned_data.get('email')

          user = User.objects.get(email=email)

          otp = random.randint(1000,9999)
       

          Otpmodel.objects.create(user_id=user,otp=otp)

# send_mail using 
          send_mail(subject = "otp for password reset",message = str(otp),from_email="swathysaji143@gmail.com",
                 recipient_list=[email])
          
          return redirect("otpverify")
          
      return render(request,"forgotpswd.html",{"form":form})
  

class Otpverifyview(View):

    def get(self,request):
        form =  OtpverifyForm()

        return render(request,"otpverify.html",{"form":form})

    def post(self,request):
        form = OtpverifyForm(request.POST)

        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            item = Otpmodel.objects.get(otp = otp)

            user_id = item.user_id
            user = User.objects.get(id = user_id.id)
            username = user.username

            if item:
                
                request.session['user'] = username

                return redirect("reset")
            
        return render(request,"otpverify.html",{"form":form})    
    

class Resetpasswordview(View):

    def get(self,request):
        form = ResetPasswordForm()

        return render(request,"resetpswd.html",{"form":form})
    
    def post(self,request):

        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')

            confirm_password = form.cleaned_data.get('confirm_password')

            if password == confirm_password:

                username= request.session.get('user')

                user= User.objects.get(username = username)

                user.set_password(password)
                user.save()

                return redirect("login")
        return render(request,"resetpswd.html")
    

# category based filter
# filtering queries
# methods: get


class Taskfilterview(View):
    def get(self,request):
        category = request.GET.get('category')  # http method get data 
        Task = TaskModel.objects.filter(user_id = request.user) # login details of all the user
        tasks = Task.filter(task_category=category) # collection
        print(tasks)
        return render (request,"filter.html",{"tasks":tasks})
    


class Indexview(View):
    def get(self,request):
        return render(request,"index.html")
