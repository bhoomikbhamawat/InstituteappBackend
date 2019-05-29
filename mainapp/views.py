from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def checkregister(request):

    response = {}
    response["status"]=0
    
    if request.method == 'POST':
        post = json.loads(request.body)#request.POST
        email = post["email"]
        try:
            student = Student.objects.get(email__iexact = email)
            response["name"]=student.name
            response["roll"]=student.roll
            response["phone"]=student.phone
            response["department"]=student.department
            response["status"]=1 #registered

        except:
            response["status"] = 2 #not registered
    return JsonResponse(response) 


@csrf_exempt
def login(request):
    response = {}
    response["status"]=0
    if request.method == 'POST':
        post = json.loads(request.body)#request.POST
        email = post["email"]
        try:
            student = Student.objects.get(email__iexact = email)
            student.roll = post["roll"]
            student.name = post["name"]
            student.phone = post["phone"]
            student.department = post["department"]
            student.fcmtoken = post["fcmtoken"]

            response["status"] = 2
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername+1))
            student = Student(user = user,email = email)
            student.roll = post["roll"]
            student.name = post["name"]
            student.phone = post["phone"]
            student.department = post["department"]
            student.fcmtoken = post["fcmtoken"]
            user.first_name = post["name"]
            password = "password1234"
            user.set_password(password)
            user.save()
            student.save()
            response["status"] = 1
    return JsonResponse(response) 
