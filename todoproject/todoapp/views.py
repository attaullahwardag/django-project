from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from .forms import postform
# Create your views here.

def index(request):
    data =  Articles.objects.all()
    return render(request,'todoapp/index.html',{'mycontent':data})

def postdata(request):
    form = postform()
    if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
             print('error form invalid!')
    return render(request,'todoapp/post.html',{'form':form})