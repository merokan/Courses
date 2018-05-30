from django.shortcuts import render, HttpResponse, redirect 
from models import *

def index(request):
    context = {
        'course_data' : Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def create(request):
    course = Course.objects.create(name= request.POST['name'], desc= request.POST['desc'])
    return redirect('/')

def show(request, course_id):
    context = {
        'course' : Course.objects.get(id=course_id)
    }
    return render(request, 'course/destroy.html', context)

def destroy(request, course_id):

    Course.objects.get(id=course_id).delete()
    return redirect('/')