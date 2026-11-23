from django.shortcuts import render,redirect
from .forms import Sign_Up
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.http import url_has_allowed_host_and_scheme

# Create your views here.
def account_register(request):
    if request.method == 'POST':
        form=Sign_Up(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your account succesfully registerd for this blog site')
            return redirect('account_login')
    else:
        form=Sign_Up()
    return render(request,'account/account_register.html',{'form':form})

def account_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Your account succesfully login for this blog site')
            next_url=request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect('post_blog')
            return redirect('show_blog')
    else:
        form=AuthenticationForm()
    return render(request,'account/account_login.html',{'form':form})

def account_logout(request):
    logout(request)
    messages.success(request,'Your account succesfully logout for this blog site')
    return redirect('show_blog')