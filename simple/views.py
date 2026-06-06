from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import database
from .serializers import database_serializer

def home(request):
    data=database.objects.all()
    ser=database_serializer(data, many= True)
    return JsonResponse(ser.data, safe=False)
    # return render(request, "home.html", {'data':data})

def individual(request, id):
    data=get_object_or_404(database, id=id)
    return render(request, "individual.html", { 'dat': data })