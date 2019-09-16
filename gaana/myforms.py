import os

from django.conf.urls import url
from django.conf.urls.static import settings, static
from django import forms
from django.db import models
from django.core.validators import FileExtensionValidator
#simple input forms.Form
#database input forms.Model
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import Album,Profile
class MyLogin(forms.Form):
    UserName=forms.CharField(max_length=100)
    Password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data['UserName']
        p=self.cleaned_data['Password']
        v=authenticate(username=u,password=p)
        #login(v)
        if v is None:
            raise forms.ValidationError('Incorrect credentials')

class Register(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    Re_Password=forms.CharField(widget=forms.PasswordInput)





    '''
    def image_url(self):

        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/gaana/bg2.jpg'
    def clean(self):
        p = self.cleaned_data['Password']
        p1 = self.cleaned_data['Re_Password']
        if p!=p1:
            raise forms.ValidationError('both password did not matches')

            '''




    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def clean(self):
        data=super(Register,self).clean()
        p=data['Password']
        p1=data['Re_Password']
        if p!= p1:
            raise forms.ValidationError('Both password did not match')
class Userprofile(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class Upprofile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['photo','city','DOB']

class AddAlbum(forms.ModelForm):
    class Meta:

        model=Album
        fields=['title','artist','genre','year','image']
