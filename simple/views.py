from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from .models import database,info
from django.contrib.auth import login,authenticate
from .serializers import database_serializer, ifo_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')

def log(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('pass')

        user=authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


  
def register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method=="POST":
        User.objects.create_user(
            username=request.POST.get('name'),
            password=request.POST.get('pass'),
        )

        return redirect('login')
    
    return render(request, 'register.html')

@login_required
def home(request):
    datab=database.objects.all()
    return render(request, "home.html", {'data':datab })

@login_required
@api_view(['GET'])
def individual(request, id):
    data=database.objects.get(id=id)
    jews=database_serializer(data)
    return Response(jews.data)
