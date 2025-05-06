from django import forms

from my_app.models import User,TaskModel

class Userregistrationform(forms.ModelForm):

    class Meta:
        model = User

        fields =['username','password','email']
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control w-75 mx-auto ","placeholder":"enter ur password"}),
            "email":forms.EmailInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur email"})
        }


# textinput stores characters  as class 

class Loginform(forms.Form):

    username = forms.CharField(max_length=100,widget = forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur username"}))
    password = forms.CharField(max_length=50,widget = forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur password"}))

    


class Taskform(forms.ModelForm):

    class Meta:
        model = TaskModel
        

        fields = ['taskname', 'due_date', 'description', 'task_category']
        widgets = {
            "taskname":forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur taskname"}),
            "due_date":forms.DateInput(attrs={"class":"form-control w-75 mx-auto ","placeholder":"enter ur duedate"}),
            "description":forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur description"})
            # "task_category":forms.TextInput(attrs={"class":"form-control w-75 mx-auto","placeholder":"enter ur task_category"}),
                

        }

# created_date,completed_status , user_id not using in this form and based on login [user_id]        


class ForgotpasswordForm(forms.Form):

    email = forms.CharField(max_length=100)


class OtpverifyForm(forms.Form):
    otp = forms.CharField(max_length=30)


class ResetPasswordForm(forms.Form):

    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)