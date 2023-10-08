from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           # print("passed")
            login(request, user)
           # print("passed")
            temp = user.employee
          #  print(temp.auto_increment_id)
            new_url = "/emp/" + str(temp.auto_increment_id) + "/"
            print(new_url)
            return redirect(new_url)           
        else:
             print("failed")
             messages.success(request, ("error"))
             return redirect('/members/login_user/')
    else:
        return render(request, 'authenticate/login.html', {})






# Create your views here.
