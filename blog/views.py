from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from blog.forms import SignupForm
from blog.forms import LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.models import Group, User

# Create your views here.
def home(req):
    post = Post.objects.all()
    return render(req,"home.html",context = {"post":post})

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contact.html")

def dashboard(req):
    if req.user.is_authenticated:
        post = Post.objects.all()
        
        user = req.user
        full_name = user.get_full_name()
        
        gps = user.groups.all()
        return render(req,"dashboard.html",{"post":post,"fnm":full_name,"gps":gps})
    else:
        return HttpResponseRedirect("/blog/user_login")
def signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='Auther')
            user.groups.add(group)
            
            messages.success(req,"Successfully Register!!!!")
            messages.warning(req,"Please login!!!")
            return HttpResponseRedirect("/blog/user_login")
    else:
        form = SignupForm()       
    
    return render(req,"signup.html",{"fm":form})

def user_login(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = LoginForm(request=req,data=req.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                up= form.cleaned_data['password']
                user = authenticate(username=uname,password=up)
                if user is not None:
                    login(req,user)
                    messages.success(req,"Login successfully!!!")
                    return HttpResponseRedirect("/blog/dashboard")
                    # return render(req,"dashboard.html")
        else:
            form = LoginForm()
        
        return render(req,"login.html",{"fm":form})
    else:
        return HttpResponseRedirect("/blog/dashboard")
def user_logout(req):
    logout(req)
    messages.success(req,"Logout successfully")
    return HttpResponseRedirect("/blog/home")
    # return render(req,"home.html")
    
def delete(req,pk):
    if req.user.is_authenticated:
        if req.method == "POST":
            pi = Post.objects.get(pk=pk)
            pi.delete()
            return HttpResponseRedirect("/blog/dashboard")
    else:
        return HttpResponseRedirect("/blog/user_login")

def update(req,pk):
    if req.user.is_authenticated:
        if req.method == "POST":
            pi = Post.objects.get(pk=pk)
            fm = PostForm(req.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(req,"Successfully Updated!!!!")
                return HttpResponseRedirect("/blog/dashboard")
        else:
            pi = Post.objects.get(pk=pk)
            fm = PostForm(instance=pi)       
        return render(req,"update.html",{"fm":fm})
    else:
        return HttpResponseRedirect("/blog/user_login")

def add(req):
    if req.user.is_authenticated:
        if req.method=="POST":
            fm = PostForm(req.POST)
            if fm.is_valid():
                fm.save()
                messages.success(req,"Successfilly Added post!!!!")
                return HttpResponseRedirect("/blog/dashboard")
        else:
            fm = PostForm()
        return render(req,"add.html",{"fm":fm})
    else:
        return HttpResponseRedirect("/blog/user_login")
    