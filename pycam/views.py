#django specific
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exemp
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#django rest framework
from rest_framework import viewsets, mixins

# models
from .models import *
from .serializers import SnippetSerializer
from .forms import UserForm


#3rd party libs
import numpy as np
import cv2



######################
#       Login        #
######################
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index')
            else:
                return HttpResponse("your account is now disabled")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        context = {'context': ''}
        return render(request, '../templates/login.html', context)


######################
#       Logout       #
######################
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



##################
#   Index Page   #
##################
def index(request):
    print("index: " + str(request.user))
    if request.user.is_authenticated:
        livestream = 'http://104.157.73.60/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER'
        context = {'camera': livestream,
                   'user': request.user,
                   'username': request.user.username}
        return render(request, '../templates/index.html', context)
    return HttpResponseRedirect('/login')


#########################
# Snippet RESTful Model #
#########################

class CRUDBaseView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass

class SnippetView(CRUDBaseView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()