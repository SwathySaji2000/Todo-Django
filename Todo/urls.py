"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_app.views import Userregisterview,Loginview,Logoutview,addtaskview,Taskreadview,Taskupdateview,Taskdeleteview,Taskdetailview,Taskedit,Forgotpasswordview,Otpverifyview,Resetpasswordview,Taskfilterview,Indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Indexview.as_view(),name="index"),
    path('todo/signup',Userregisterview.as_view(),name="signup"),

    path('login/',Loginview.as_view(),name="login"),
    path('logout/',Logoutview.as_view(),name="logout"),
    path('task/addtask/',addtaskview.as_view(),name="add_task"),
    path('task/list/',Taskreadview.as_view(),name="task_list"),
    path('task/update/<int:pk>',Taskupdateview.as_view(),name="update"),
    path('task/delete/<int:pk>',Taskdeleteview.as_view(),name="delete"),
    path('task/<int:pk>/detail/',Taskdetailview.as_view(),name="detail"),
    path('todo/taskedit/<int:pk>',Taskedit.as_view(),name="edit"),
    path('todo/forgotpswd/',Forgotpasswordview.as_view(),name="forgotpsd"),
    path('todo/otp_verify/',Otpverifyview.as_view(),name = "otpverify"),
    path('todo/resetpswd/',Resetpasswordview.as_view(),name="reset"),
    path('todo/filter/',Taskfilterview.as_view(),name="filter"),
    
    ]