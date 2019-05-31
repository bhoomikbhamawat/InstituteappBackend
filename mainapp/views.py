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
            response["year"] = student.year
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
            student.year = post["year"]
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
            student.year = post["year"]
            user.first_name = post["name"]
            password = "password1234"
            user.set_password(password)
            user.save()
            student.save()
            response["status"] = 1
    return JsonResponse(response) 


@csrf_exempt
def feed(request):
    response = {}
    response["status"]=0
    if request.method == 'POST':
        post = json.loads(request.body)#request.POST
        roll = post["roll"]
        student = Student.objects.get(roll=roll)
        notifs=Notification.objects.all()
        # print(notifs.viewedby_set.all())
        if student:
            for notif in notifs:
                # try:
                    if not (student in notif.viewedby.all()):
                        notif.viewedby.add(student)
                        notif.save()
                        print("2132133333333333333333333333333333333333333333333333")
                # except:
                #         notif.viewedby.add(student)
                #         notif.save()
            outnotif=[]

            for notif in notifs:
                curr={}
                curr["club"]=notif.clubname.name
                curr["council"]=notif.clubname.councilname.name
                curr["title"]=notif.notification_header
                curr["description"]=notif.notification
                if notif.notification_pic:
                    curr["image"]=notif.notification_pic.url
                curr["datetime"]=notif.datetime
                curr["location"]=notif.location
                curr["viewedcount"]=notif.viewedby.count()

                outnotif.append(curr)

            response["status"]=1
            response["notif"]=outnotif
            return JsonResponse(response)

        else:
            return JsonResponse(response) 

    return JsonResponse(response)

      