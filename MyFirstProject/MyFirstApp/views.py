from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context={
        "firstName":"Sumit",
        "lastName":"Kamboj"
    }
    return render(request,"index.html",context)       # we are rendering file of template folder
def lambdaFun(request):
    return HttpResponse("Lambda Function")
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')