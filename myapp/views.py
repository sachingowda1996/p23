from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.
def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h3>Topic added successfully</h3>")
        else:
            return HttpResponse("<h3>Topic already added</h3>")
    return render(request,"create_topic.html")
def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get('url')    
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t, name=name, url=url)[0]
        w.save()
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})
                   
