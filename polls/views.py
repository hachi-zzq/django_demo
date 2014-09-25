from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from polls.models import User
import os
import datetime
from django import forms

def home(request):
    return HttpResponse(User.objects.all().values_list('id','username'))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=48)


def index(request):
    return HttpResponse('index')


def dec(request):
    return HttpResponse('dec')