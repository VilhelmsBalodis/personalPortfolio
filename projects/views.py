from django.shortcuts import render
from .models import Project

def home(request):
    project = Project.objects.all()
    return render(request, 'projects/home.html',{'project':project})