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

def homeview(request):
    allpost=devoloperprofile.objects.all()
    return render(request,'YouTeamapp/home.html',{'allpost':allpost})

def viewprofile(request):
    allpost=devoloperprofile.objects.all()
    return render(request,'YouTeamapp/profile2.html',{'allpost':allpost})

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
        else:
            return render(request, 'YouTeamapp/signup.html',
                          {'msg': "Already Exist This Username", 'sform': sform})



def autheview(request):
    if request.user.is_authenticated:
        try:
            user=User.objects.get(id=request.user.id)
            user_profile=devoloperprofile.objects.get(pk=user.id)
        # free=Freemodel.objects.get(pk=user.id)
        except devoloperprofile.DoesNotExist:
            if request.method == 'GET':
                try:
                    profileob = profileForm()
                except profileForm.DoesNotExist:
                    return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your Profile"})
                else:
                    return render(request, 'YouTeamapp/profile.html', {'pform': profileob ,'msg':'Add Your Profile'})
            if request.method == 'POST':
                profileob = profileForm(request.POST, request.FILES)
                # if profileob.is_save():
                if profileob.is_valid():
                    post = profileob.save(commit=False)
                    post.save()
                    # profileob.save(update=True)
                    return render(request, 'YouTeamapp/succes.html', {'msg': "Added Your Profile"})
                if ValueError:
                    return render(request, 'YouTeamapp/succes.html', {'msg': "Already Add Profile "})


        # try:
        #     user_exp = devlopertechnical.objects.get(user_exp_id=user.id)
        # except devlopertechnical.DoesNotExist:
        #     return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your  Technical Profile"})  'user_exp':user_exp,
        #suser_tech=technology.objects.get(user_tech_id=user.id)
        else:
            return render(request,'YouTeamapp/free.html',{"user":user,"user_profile":user_profile,})
    # else:
    #     return render(request,'YouTeamapp/succes.html',{'msg':"please complete your profile"})


def authenticatedview(request):
    if request.user.is_authenticated:
        try:
            user=User.objects.get(id=request.user.id)
            user_exp = devlopertechnical.objects.get(user_exp_id=user.id)
        except devlopertechnical.DoesNotExist:
            if request.method == 'GET':
                try:
                    tform = devlopertechnicalForm()
                except devlopertechnicalForm.DoesNotExist:
                    return render(request, 'YouTeamapp/succes.html', {'msg': "already add information...!!!"})
                else:
                    return render(request, 'YouTeamapp/expirence.html', {'tform': tform})
            if request.method == 'POST':
                tform = devlopertechnicalForm(request.POST)
                if tform.is_valid():
                    tform.save()
                    return render(request, 'YouTeamapp/succes.html', {'msg': "Added Your Expirence"})

                if ValueError:
                    return render(request, 'YouTeamapp/succes.html', {'msg': "Already Add Profile "})

                else:
                    return render(request, 'YouTeamapp/succes.html', {'msg': "already add information...!!!"})
        else:
            return render(request,'YouTeamapp/expirence0.html',{"user":user,'user_tech':user_exp,})

def allpostview(request):
    allpost=devoloperprofile.objects.all()
    user=User.objects.get(id=request.user.id)
    # user_exp=devlopertechnical.objects.get(user_exp_id=user.id)'techno':user_exp}
    return render(request,'YouTeamapp/allprofile.html',{'allpost':allpost})



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
        # user=User.objects.get(id=request.user.id)
        profileob=profileForm(request.POST,instance=user_profile)
        #return render(request,'YouTeamapp/check.html',{'form':form})
        # post = Post(text=eform, author=request.user)
        if profileob.is_valid():
            save=profileob.save()
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














# @login_required
# def profileview(request):
#     profile=devoloperprofile.objects.all()
#     if request.method=='GET':
#         try:
#             profileob=profileForm()
#         except profileForm.DoesNotExist:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your Profile"})
#         else:
#             return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     if request.method=='POST':
#         profileob=profileForm(request.POST,request.FILES)
#        #if profileob.is_save():
#         if profileob.is_valid():
#             post = profileob.save(commit = False)
#             post.save()
#                 # profileob.save(update=True)
#             return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
#         if ValueError:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Already Add Profile "})
#
#         # else:
#         #     return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     # else:
#     #         profileob=profileForm()
#     #         return render(request,'YouTeamapp/profile.html',{'profile': profile})
#     #




# def profileview(request):
#     profile=devoloperprofile.objects.all()
#     if request.method=='GET':
#         try:
#             profileob=profileForm()
#         except profileForm.DoesNotExist:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your Profile"})
#         else:
#             return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     if request.method=='POST':
#         profileob=profileForm(request.POST,request.FILES)
#        #if profileob.is_save():
#         if profileob.is_valid():
#             post = profileob.save(commit = False)
#             post.save()
#                 # profileob.save(update=True)
#             return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
#         if ValueError:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "All Ready Add Profile"})
#
#         # else:
#         #     return render(request,'YouTeamapp/profile.html',{'pform':profileob})
#     # else:
#     #         profileob=profileForm()
#     #         return render(request,'YouTeamapp/profile.html',{'profile': profile})
#     #





#technical information form
# @login_required
# def devlopertechnicalview(request):
#     if request.method=='GET':
#         try:
#             tform=devlopertechnicalForm()
#         except devlopertechnicalForm.DoesNotExist:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "already add information...!!!"})
#         # try:
#         #     tform=devlopertechnical()
#         # except devlopertechnical.ValueError:
#         #     return render(request, 'YouTeamapp/succes.html', {'msg': "already add information...!!!"})
#         else:
#             return render(request,'YouTeamapp/expirence.html',{'tform':tform})
#     if request.method=='POST':
#         tform=devlopertechnicalForm(request.POST)
#         if tform.is_valid():
#             tform.save()
#             return render(request,'YouTeamapp/succes.html',{'msg':"ragistration succes"})
#
#         if ValueError:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Already Add Profile "})
#
#         else:
#             return render(request,'YouTeamapp/succes.html',{'msg':"already add information...!!!"})
#







# user profile view
# def autheview(request):
#     if request.user.is_authenticated:
#         try:
#             user=User.objects.get(id=request.user.id)
#             user_profile=devoloperprofile.objects.get(pk=user.id)
#         # free=Freemodel.objects.get(pk=user.id)
#         except devoloperprofile.DoesNotExist:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your Profile....!!!!"})
#         try:
#             user_exp = devlopertechnical.objects.get(user_exp_id=user.id)
#         except devlopertechnical.DoesNotExist:
#             return render(request, 'YouTeamapp/succes.html', {'msg': "Please Add Your  Technical Profile"})
#         #suser_tech=technology.objects.get(user_tech_id=user.id)
#         else:
#             return render(request,'YouTeamapp/free.html',{"user":user,"user_profile":user_profile,'user_exp':user_exp,})
#     else:
#         return render(request,'YouTeamapp/succes.html',{'msg':"please complete your profile"})




