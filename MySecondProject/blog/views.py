from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

contact={
        'address':"Jalalabad",
        'mobile_no':'123456789'
}

context=Post.objects.all().values()[0]
def home(request):
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
def base(request):
    return render(request,'blog/base.html')