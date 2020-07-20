from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
# Create your views here.

def usersignup(req):
    if req.method == "GET":
        return render(req,'signup.html',{'form':UserCreationForm()})
    else:
      #  print(req.POST["username"],req.POST["password1"],req.POST["password2"])
      if req.POST['password1'] == req.POST['password2']:
        try:
            user = User.objects.create_user(req.POST["username"],password=req.POST["password1"])
            user.save()
            login(req,user)
            return redirect('home')
        except IntegrityError:
             return render(req,'signup.html',{'form':UserCreationForm(),'error':"please choose different username"})

      else :
        return render(req,'signup.html',{'form':UserCreationForm(),'error':"password dont match"})


def userlogin(req):
  if req.method == 'GET':
     return render(req,'login.html',{'form':AuthenticationForm()})
  else:
    user = authenticate(username=req.POST["username"],password=req.POST["password"])
    if user is None:
          return render(req,'login.html',{'form':AuthenticationForm(),'error':"username or password is incorrect"})
    else:
      login(req,user)
      return redirect('home')


def userlogout(req):
  logout(req)
  return redirect('userlogin')
