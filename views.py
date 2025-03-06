from django.shortcuts import render, redirect
from entry.models import *

# Create your views here.

def form(request):
    if request.method == "POST":

        data=request.POST
        name=data.get('blogName')
        description=data.get('description')
        image= request.FILES.get('image')
        
    
        Blogname.objects.create(
            blogname=name,
            description=description,
            image=image,
        )
        return redirect('/blg/')
    queryset = Blogname.objects.all()
    
    return render(request,'form.html', context = {'blog_data' : queryset})
    


def blg(request):
    priyanshu = Blogname.objects.all()

    return render(request,'blg.html', context = {'blog_data' : priyanshu})