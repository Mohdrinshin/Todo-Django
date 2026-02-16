from django.shortcuts import render , redirect
from django.views.generic import View
from app.forms import *
from app.models import *
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.utils.decorators import method_decorator

def is_user(fn): #def get

    def wrapper(request,**kwargs):

        id = kwargs.get("pk")

        item =TaskModel.objects.get(id=id)

        if item.user_id == request.user:

            return fn(request,**kwargs)
        
        return redirect("login")
    
    return wrapper

class UserRegistorView(View):

    def get(self,request):

        form = UserForm

        return render(request,"signup.html",{'form':form})
    
    def post(self,request):

        form = UserForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            username = form.cleaned_data.get('username')

            email = form.cleaned_data.get('email')

            password = form.cleaned_data.get('password')

            # or

            # user.objects.create_user(**form.cleaned_data)

            User.objects.create_user(username=username,email=email,password=password)

        form = UserForm

        # return render(request,'signup.html',{'form':form})

        return redirect ("login")
    
class LoginView(View):

    def get(self,request):

        form = LoginForm

        return render(request,"login.html",{"form":form})
    
    def post(self,request):

        form = LoginForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            username = form.cleaned_data.get("username")

            password = form.cleaned_data.get("password")

            user_login = authenticate(request,username=username,password=password)

            if user_login:

                login(request,user_login)

                return redirect("readTask")
            
            else :

                form = LoginForm

                return render(request,"login.html",{"form":form})
            
class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("login")
    
class AddView(View):

    def get(self,request):

        form = TaskForm

        return render(request,"add.html",{'form':form})
    
    def post(self,request):

        form = TaskForm(request.POST) 

        if form.is_valid():

            print(form.cleaned_data)

            TaskModel.objects.create(user_id=request.user,**form.cleaned_data) # user_id ithine kaattilum better option user aanu ex:- user_id=request.user) better user = request.user aanu

        form = TaskForm

        return redirect("readTask")
    
# @method_decorator(decorator=is_user,name="dispatch")

class ReadView(View):

    def get(self,request):

        data = TaskModel.objects.filter(user_id=request.user)

        return render(request,"readTask.html",{'data':data})
    
@method_decorator(decorator=is_user,name="dispatch")
    
class Update(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        data = TaskModel.objects.get(id=id)

        form = TaskForm(instance=data)

        return render(request,"update.html",{'form':form})
    
    def post(self,request,**kwargs):

        id = kwargs.get('pk')

        data = TaskModel.objects.get(id=id)

        form = TaskForm(request.POST,instance=data)

        if form.is_valid():

            form.save()

        return redirect("readTask")
    
@method_decorator(decorator=is_user,name="dispatch")
    
class Delete(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        item = TaskModel.objects.get(id=id)

        item.delete()

        return redirect("readTask")
    
@method_decorator(decorator=is_user,name="dispatch")
    
class TaskSpecific(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        item = TaskModel.objects.filter(id=id)

        return render(request,"specific.html",{'item':item})
    
class Completed_status(View):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        data = TaskModel.objects.get(id=id)

        data.completed_status =True

        data.save()

        return redirect("readTask")
    
class ForgetView(View):

    def get(self,request):

        form = ForgetForm

        return render(request,"forget.html",{'form':form})
    
    def post(self,request):

        form = ForgetForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            email = form.cleaned_data.get('email')

            user = User.objects.get(email=email)

            otp = random.randint(1000,9999)

            OtpModel.objects.create(user_id=user,otp=otp)

            send_mail(subject="otp for password reset",message=str(otp),from_email="mohammedrinshin1@gmail.com",recipient_list=[email])

            # return render(request,"forget.html",{'form':form})

            return redirect('otp')

class Otp(View):

    def get(self,request):

        form = OtpForm

        return render(request,'otp.html',{'form':form})
    
    def post (self,request):

        form = OtpForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            otp = form.cleaned_data.get('otp')

            item = OtpModel.objects.get(otp=otp)

            user_id = item.user_id

            user = User.objects.get(id=user_id.id)

            username = user.username

            if item:

                # store the user id in session so ResetView can look up the user by id
                request.session['user'] = user.id

                return redirect('reset')
            
            # form = OtpForm
            
        return render(request,"otp.html",{'form':form})
    
class ResetView(View):
    
    def get(self,request):

        form = ResetpasswordForm

        return render(request,"reset.html",{"form":form})
    
    def post(self,request):

        form =ResetpasswordForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data.get('password')

            confirm_password = form.cleaned_data.get('confirm_password')

            if password == confirm_password:

                user_id = request.session.get('user')

                user = User.objects.get(id=user_id)

                user.set_password(password)

                user.save()

                del request.session['user']

                return redirect("login")
            
        return render(request,"reset.html",{"form":form})

class TaskFilter(View):

    def get(self,request):

        category = request.GET.get('category')

        task = TaskModel.objects.filter(user_id = request.user)

        tasks = task.filter(task_category = category)

        print(tasks)

        return render(request,"filter.html",{'tasks':tasks})
    
def home(request):
    
    return render(request,"base.html") 


class IndexView(View):

    def get(self,request):

        return render(request,"index.html")
    
