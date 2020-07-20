from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.


def home(req):
    blogs =  Blog.objects.order_by("-date")
    return render(req,'home.html',{'blogs':blogs})

def about(req):
    return render(req,'about.html')

def detail(req,id):
    blog = get_object_or_404(Blog,pk=id)
    return render(req,'detail.html',{'blog':blog})

