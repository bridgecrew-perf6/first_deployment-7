from tokenize import group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import SignupForm,LoginForm,AddForm,SetPassword
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from . models import Post
from django.contrib.auth.models import Group

# Create your views here.
def base(request):
    posts=Post.objects.all()

    return render(request,'home.html',{'post':posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dash(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name() # this method combine first and last name of user and returns full_name 
        gps=user.groups.all() # returns all the group

        return render(request,'dashboard.html',{'post':posts,'fullname':full_name,'gp':gps})
    else:
        return HttpResponseRedirect('/login')

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
        
            user=form.save()
            group=Group.objects.get(name='Author') 
            user.groups.add(group)
            messages.success(request,'congratulations ! your account has created successfully')

        
    else:

        form=SignupForm() 

    return render(request,'signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'successfully logged in')
                    return HttpResponseRedirect('/dashboard/')
        else:

            form=LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form=AddForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request,'post added successfully')
            form=AddForm()
            
        else:
            form=AddForm()
        return render(request,'addpost.html',{'form':form})
        
    else:

        return HttpResponseRedirect('/login')


def update(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            up=Post.objects.get(pk=id)
            form=AddForm(request.POST,instance=up)
            if form.is_valid():
                form.save()
                messages.info(request,'Post updated')
            return HttpResponseRedirect('/dashboard')
        else:
            up=Post.objects.get(pk=id)
            form=AddForm(instance=up)

        return render(request,'updatepost.html',{'form':form})
        
    else:

        return HttpResponseRedirect('/login')

def delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
           pd= Post.objects.get(pk=id)
           pd.delete()
           messages.success(request,'post nolonger available')

       
        return HttpResponseRedirect('/dashboard')
    else:

        return HttpResponseRedirect('/login')


def password(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
        
            form=SetPassword(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                
                
                messages.success(request,'Password Changed Successfully..')
                return HttpResponseRedirect('/dashboard')
        else:
            form=SetPassword(user=request.user)

        return render(request,'password.html',{'form':form})
    # else:
    #     return HttpResponseRedirect('/password')