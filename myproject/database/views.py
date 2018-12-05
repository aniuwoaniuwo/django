from django.shortcuts import render
from django.http import HttpResponse
from database.models import classification,data

def index(request):
    classifications=classification.objects.all()
    return render(request,'index.html',{'classifications':classifications})

def classindex(request,classification_slug):#(?P<classification_slug>[^/]+)，<>里面的是id，传id后面的数据到views作为参数
    classification1=classification.objects.get(slug=classification_slug)
    return render(request,'classindex.html',{'classification1':classification1})

def dataindex(request,data_slug):
    data1=data.objects.get(slug=data_slug)
    return render(request,'dataindex.html',{'data1':data1})
