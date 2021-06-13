from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog


def all_blogs(request):
    blogs=blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blo':blogs})

def details(request,blog_id):
    blogs=get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/details.html',{'blo':blogs})
