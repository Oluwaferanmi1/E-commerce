from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.html',{'name':'Feranmi'})

# Create your views here.

# views is the request handler