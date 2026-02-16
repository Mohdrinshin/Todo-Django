from django import forms
from app.models import *

class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['email','password','username']

        widgets = {

            "username" :forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter your username"}),
            "password" : forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter password"}),
            "email" : forms.EmailInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter email"})
        }

class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter Your username"}
    ))

    password = forms.CharField(max_length=100 ,widget=forms.PasswordInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter password"}
    ))

class TaskForm(forms.ModelForm):

    class Meta:
        
        model = TaskModel

        exclude = ['created_date','completed_status','user_id']

        widgets = {
            "taskname": forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter Your Task Name"}),
            "due_date" :forms.DateInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter Date"}),
            "description" : forms.Textarea(attrs={"class":"form-control w-50  mx-auto","placeholder":"Enter Description *option"}),
            "task_category" : forms.Select(attrs={"class":"form-control w-50 mx-auto", "placeholder":"category"})
        }

        def __init__(self, *args, **kwargs):
            
          super().__init__(*args, **kwargs)
          self.fields["task_category"].empty_label = "Select Category"

class ForgetForm(forms.Form):

    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter Your Email"}
    ))

class OtpForm(forms.Form):

    otp = forms.IntegerField(widget=forms.NumberInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter Your Otp"}
    ))

class ResetpasswordForm(forms.Form):
    
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter New Password"}
    ))

    confirm_password = forms.CharField(max_length=50 ,widget=forms.PasswordInput(
        attrs={"class":"form-control w-50 mx-auto","placeholder":"Confirm New Password"}
    ))