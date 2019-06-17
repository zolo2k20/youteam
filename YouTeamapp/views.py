# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from YouTeamapp.forms import *
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
#from django.contrib.auth.models import User
# Email sending.
from django.core.mail import send_mail
from django.conf import settings
#from django import ipdb
#from .filters import TechnologyFilter
# Create your views here.
# def homeview(request):
#     allpost=devoloperprofile.objects.all()
#     return render(request,'YouTeamapp/profile2.html',{'allpost':allpost})

def homeview(request):
    allpost=devoloperprofile.objects.all()
    return render(request,'YouTeamapp/profile1.html',{'allpost':allpost})

def viewprofile(request):
    allpost=devoloperprofile.objects.all()
    return render(request,'YouTeamapp/profile2.html',{'allpost':allpost})



def language(request):
    form=techForm()
    return render(request,'YouTeamapp/language.html')

def clientview(request):
    client=clientprofile.objects.all()
    return render(request,'YouTeamapp/client.html',{'client':client})

def freeview(request):
    return render(request,'YouTeamapp/ac_sent.html')

# Devloper signup Form view
def signupview(request):
    if request.method=='GET':
        sform= SignupdevloperForm()
        return render(request,'YouTeamapp/signup.html',{'sform':sform})
    if request.method=='POST':
        # subject = 'Django Email Subject' #email sending
        # message = 'Thank you for register'
        # email_from = settings.EMAIL_HOST_USER
        sform= SignupdevloperForm(request.POST)
        if sform.is_valid():
            user=sform.save()
            # recipient_list=[user.email,]
            user.set_password(user.password)
            user.save()
            # print("Email: ",recipient_list)
            # send_mail(subject,message,email_from,recipient_list)
        #return render(request,'YouTeamapp/succes.html',{'msg':"ragistration sucess"})
        # else:
        #     sform= SignupdevloperForm()
        #     return render(request,'YouTeamapp/signup.html',{'msg':"please enter valid username and password....",'sform':sform})
        return HttpResponseRedirect(reverse('login'))

# Client signup Form view
def signupclientview(request):
    if request.method=='GET':
        scform=signupclientForm()
        return render(request,'YouTeamapp/signup.html',{'scform':scform})
    if request.method=='POST':
        scform=signupclientForm(request.POST)
        if scform.is_valid():
            suser=scform.save()
            suser.set_password(suser.password)
            suser.save()
        #return render(request,'YouTeamapp/succes.html',{'msg':"ragistration sucess"})
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request,'YouTeamapp/signup.html',{'msg':"please enter valid username and password....",'scform':scform})


#technical information form
@login_required
def devlopertechnicalview(request):
    if request.method=='GET':
        tform=devlopertechnicalForm()
        return render(request,'YouTeamapp/expirence.html',{'tform':tform})
    if request.method=='POST':
        tform=devlopertechnicalForm(request.POST)
        if tform.is_valid():
            tform.save()
            return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
        else:
            return render(request,'YouTeamapp/succes.html',{'msg':"already add information"})

# user profile form
# @login_required
# def profileview(request):
#     profile=devoloperprofile.objects.all()
#     if request.method=='GET':
#         profileob=profileForm()
#         return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     if request.method=='POST':
#         profileob=profileForm(request.POST,request.FILES)
#        #if profileob.is_save():
#         if profileob.is_valid():
#             post = profileob.save(commit = False)
#             post.save()
#                 # profileob.save(update=True)
#             return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
#         else:
#             return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     else:
#             profileob=profileForm()
#             return render(request,'YouTeamapp/profile.html',{'profile': profile})



@login_required
def clientprofileview(request):
    if request.method=='GET':
        cform=clientprofileFrom()
        return render(request,'YouTeamapp/clientprofile.html',{'cform':cform})
    if request.method=='POST':
       cform=clientprofileFrom(request.POST)
       if cform.is_valid():
           cform.save()
           return render(request,'YouTeamapp/succes.html',{'msg':"client informatiom complete....."})
       else:
           return render(request,'YouTeamapp/succes.html',{'msg':"please submit valid form"})
# all profile view
def allpostview(request):
    allpost=devoloperprofile.objects.all()
    user=User.objects.get(id=request.user.id)
    # user_exp=devlopertechnical.objects.get(user_exp_id=user.id)'techno':user_exp}
    return render(request,'YouTeamapp/allprofile.html',{'allpost':allpost})

# user profile view
def autheview(request):
    if request.user.is_authenticated:
        user=User.objects.get(id=request.user.id)
        user_profile=devoloperprofile.objects.get(pk=user.id)
        user_exp=devlopertechnical.objects.get(user_exp_id=user.id)
        # free=Freemodel.objects.get(pk=user.id)
        #suser_tech=technology.objects.get(user_tech_id=user.id)
        return render(request,'YouTeamapp/free.html',{"user":user,"user_profile":user_profile,'user_exp':user_exp,})
    else:
        return render(request,'YouTeamapp/succes.html',{'msg':"please complete your profile"})


def authenticationview(requset):
    if request.user.is_authenticated:
        user=User.objects.get(id=request.user.id)
        client_profile=clientprofile.objects.get(id=user.id)
        return render(request,'YouTeamapp/clientpr.html',{'client_profile':client_profile})



# def alltpost(request):
#     if request.user.is_authenticated:
#         user=User.objects.get(id=request.user.id)
#         user_tech=technology.objects.get(user_tech_id=user.id)
#         return render(request,'YouTeamapp/techf.html',{"user":user,"user_tech":user_tech})


def deletepost(request):
    user=User.objects.get(id=request.user.id)
    #delate=Expirence.objects.get(user_tech_id=user.id)
    user_profile=devoloperprofile.objects.get(customer_id=user.id)
    # dela=profile.objects.get(id=pid)
    #delate.delete()
    user_profile.delete()
    return render(request,'YouTeamapp/succes.html',{'msg':'delete successfuly'})
def deletetechnical(request):
    user=User.objects.get(id=request.user.id)
    user_tech1=devlopertechnical.objects.get(user_exp_id=user.id)
    user_tech1.delete()
    return render(request,'YouTeamapp/succes.html',{'msg':'delete successfuly'})

# Edit user profile informatiom
def edit(request):
    user=User.objects.get(id=request.user.id)
    user_profile=devoloperprofile.objects.get(customer_id=user.id)
    if request.method=='GET':
        return render(request, 'YouTeamapp/check.html', {"user_profile":user_profile})
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        user_profile=profileForm(request.POST,instance=user_profile)
        #return render(request,'YouTeamapp/check.html',{'form':form})
        # post = Post(text=eform, author=request.user)
        if user_profile.is_valid():
            save=user_profile.save()
            return render(request,'YouTeamapp/succes.html',{'msg':"update Successfully"})
        # else:
        #     return render(request,'YouTeamapp/succes.html',{'msg':"already same da"})

# Edit user technical information informatiom
def edittechnology(request):
    user=User.objects.get(id=request.user.id)
    user_tech1=devlopertechnical.objects.get(user_exp=user.id)
    if request.method=='GET':
        return render(request, 'YouTeamapp/technologyedit.html', {"user_tech1":user_tech1})
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        eform=devlopertechnicalForm(request.POST,instance=user_tech1)
        #return render(request,'YouTeamapp/check.html',{'form':form})


        if eform.is_valid():
            eform.save()
            return render(request,'YouTeamapp/succes.html',{'msg':"update Successfully"})

def updatecpview(request,pk):
    clintform=clientprofile.objects.get(id=pk)
    if request.method=='GET':
        return render(request,'YouTeamaap/update.html',{'clintform':clintform})
    if request.method=='POST':
        cform=clientprofileFrom(request.POST,instance=clintform)
        if cform.is_valid():
            cform.save()
            return render(request,'YouTeamapp/succes.html',{'msg':"update Successfully"})


# def account_activation_sent(request):
#     return render(request, 'JJavaScript developer with over 8 years of experience in web development, use Python for server side. I am well-organized, always plan my work and tasks to deliver them in time.
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidtotob64))
#         user = User.objects.get(id=uid)
#     except (TypeError, ValueError, OverflowErrorto, User.DoesNotExist):
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)to
#         return redirect('homeview')
#     else:
#         return render(request, 'YouTeamapp/ac_invalid.html')

def search(request):
    user_list = devlopertechnical.objects.all()
    user_filter = TechnologyFilter(request.GET, queryset=user_list)
    return render(request, 'Youteamapp/search.html', {'filter': user_filter})



def profileview(request):
    if request.user.is_authenticated:
        user=User.objects.get(id=request.user.id)
        user_profile=devoloperprofile.objects.get(customer_id=user.id)
        if User.objects.filter(username=user).exists():
            # return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
            if(user_profile.Pic == user_profile.Datetime == user_profile.Designation== user_profile.complete_project ==user_profile.salary_year  ==user_profile.salary_month ==user_profile.salary_hour==user_profile.City==user_profile.State==user_profile.Zip_code==user_profile.offical_email==user_profile.LinkedIn_profile_url==user_profile.cover==user_profile.customer==null ):
            # if devoloperprofile.objects.filter(user=user_profile).exists():
                if request.method=='GET':
                    profileob=profileForm()
                    return render(request,'YouTeamapp/profile.html',{'pform':profileob})
                if request.method=='POST':
                    profileob=profileForm(request.POST,request.FILES)
       #if profileob.is_save():
                    if profileob.is_valid():
                        post = profileob.save(commit = False)
                        post.save()
                # profileob.save(update=True)
                        return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
                    else:
                        return render(request,'YouTeamapp/profile.html',{'pform':profileob})
            elif request.method=='GET':
                return render(request, 'YouTeamapp/check.html', {"user_profile":user_profile})
            if request.method=='POST':
                user=User.objects.get(id=request.user.id)
                user_profile=profileForm(request.POST,instance=user_profile)
            #return render(request,'YouTeamapp/check.html',{'form':form})
            # post = Post(text=eform, author=request.user)
                if user_profile.is_valid():
                    save=user_profile.save()
                    return render(request,'YouTeamapp/succes.html',{'msg':"update Successfully"})




def freeview(request):
    if request.user.is_authenticated:
        user=User.objects.get(id=request.user.id)
        # free=Freemodel.objects.get(pk=user.id)
        if request.method=='GET':
            form=FreeForm12()
            return render(request,'YouTeamapp/profile.html',{'pform':form})
        if request.method=='POST':
            form=FreeForm12(request.POST,request.FILES)
#if profileob.is_save():
            if form.is_valid():
                post = form.save(commit = False)
                post.save()
    # profileob.save(update=True)
                return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})


