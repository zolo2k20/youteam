from django import forms
from YouTeamapp.models import *
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

class SignupdevloperForm(forms.ModelForm):
    full_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=60,help_text='Required a valid email addresss')
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    mobile_number=forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'7777778888'})
    )
    country=forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'india'})
    )
    check_me_out=forms.BooleanField(required=True)
    class Meta:
        model=User
        fields=('full_name','email','mobile_number','country','username','password')

    def clean(self):
        cleaned_data = super(SignupdevloperForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class signupclientForm(forms.ModelForm):
    full_name=forms.CharField()
    email=forms.EmailField(max_length=60,help_text='Required a valid email address')
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    mobile_number=forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'9999999999'})
    )
    company_name=forms.CharField(max_length=100)
    country=forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':'india'})
    )
    check_me_out=forms.BooleanField(required=True)
    class Meta:
        model=User
        fields=('full_name','email','mobile_number','company_name','country','username','password')

    def clean(self):
        cleaned_data = super(signupclientForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class devlopertechnicalForm(forms.ModelForm):
    framework=forms.CharField(required=False)
    expirencefw=forms.CharField(required=False)
    frontend_technology=forms.CharField(required=False)
    expirenceft=forms.CharField(required=False)
    other_skills=forms.CharField(required=False)
    expirenceos=forms.CharField(required=False)
    data_base=forms.CharField(required=False)
    expirencedb=forms.CharField(required=False)
    development_tools=forms.CharField(required=False)
    operating_system=forms.CharField(required=False)
    programing_language=forms.CharField(required=True)
    expirencepl=forms.CharField(required=True)
    # frontend_technology=forms.CharField(required=False)
    # expirenceft=forms.CharField(required=False)
    class Meta:
        model=devlopertechnical
        fields='__all__'
class profileForm(forms.ModelForm):

    # customer = forms.CharField(required=False)
    City=forms.CharField(required=False)
    State=forms.CharField(required=False)
    Zip_code=forms.CharField(required=False)
    LinkedIn_profile_url=forms.CharField(required=False)
    class Meta:
        model=devoloperprofile
        fields='__all__'
class clientprofileFrom(forms.ModelForm):
    class Meta:
        model=clientprofile
        fields='__all__'

class FreeForm12(forms.ModelForm):
    class Meta:
        model=Freemodel
        fields='__all__'
