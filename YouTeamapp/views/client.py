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


from django.core.mail import send_mail
from django.conf import settings

def clientview(request):
    client=clientprofile.objects.all()
    return render(request,'YouTeamapp/client.html',{'client':client})


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


# def authenticationview(requset):
#     if request.user.is_authenticated:
#         user=User.objects.get(id=request.user.id)
#         client_profile=clientprofile.objects.get(id=user.id)
#         return render(request,'YouTeamapp/clientpr.html',{'client_profile':client_profile})

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



def email(request):
    subject = 'Django Email Subject'
    message = 'Thank you for register'
    email_from = settings.EMAIL_HOST_USER

    recipient_list = ['gurjarraviiet2k13@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    # return Response(status=status.HTTP_200_OK)
    return redirect('clientview')
