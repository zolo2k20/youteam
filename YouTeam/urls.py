"""YouTeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import settings
from django.conf.urls.static import static
from django.contrib import admin
from YouTeamapp import views
from django.conf.urls import url, include
from django.views.generic import TemplateView
#from  import views as update_views
#rom YouTeamapp import views as update_views
from YouTeamapp.views import developer
from YouTeamapp.views import client


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    # devloper urls
    url('home/', developer.homeview),  # home page
    url('viewprofile/', developer.viewprofile),
    # url('tech/', developer.devlopertechnicalview),
    url('all/', developer.allpostview),
    url('deletepost/', developer.deletepost),
    url('deletetech/', developer.deletetechnical),
    url('sigh/', developer.signupview),  # signup for devloper
    url('techedit/', developer.edittechnology),
    url('edit/', developer.edit),
    # url('updatepost/<pid>', developer.edit),
    url('deletepost/', developer.deletepost),
    url('deletetech/', developer.deletetechnical),
    url('free/', developer.autheview),
    # url('profile/', developer.profileview),
    url('techview/', developer.authenticatedview),

    # client urls
    url('sigh2/', client.signupclientview),  # signup for client
    # url('button/', views.buttonview),
    url('all121/', client.clientprofileview),
    url('client/', client.clientview),
    # url('auth/', client.authenticationview),

    url('email1/', client.email),
    #
    # url('ravi/', ravi.Helloview),
    # url('FreeForm', views.freeview,),
    # url('dev/', views.devview),
    # url('updateemp/<id>', views.updatecpview),
    # url(r'^search/', views.search, name='search'),

    # url(r'^admin/', admin.site.urls),
    #
    # url('sigh/',views.signupview),# signup for devloper
    # url('sigh2/',views.signupclientview),# signup for client
    # # url('button/', views.buttonview),
    # url('home/', views.homeview),# home page
    # url('client/', views.clientview),
    # url('auth/', views.authenticationview),
    # url('viewprofile/', views.viewprofile),
    # url('techedit/', views.edittechnology),
    # url('tech/', views.devlopertechnicalview),
    # url('edit/', views.edit),
    # url('all/', views.allpostview),
    # #url('lang/', views.alltpost),
    # url('profile/', views.profileview),
    #
    # url('FreeForm', views.freeview,),
    # #url('dev/', views.devview),
    # url('deletepost/', views.deletepost),
    # url('deletetech/', views.deletetechnical),
    #  url('updateemp/<id>', views.updatecpview),
    # url('free/', views.autheview),
    #
    # url('all121/', views.clientprofileview),
    # url('accounts/',include('django.contrib.auth.urls')),
    # url(r'^search/', views.search, name='search'),
    #


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
