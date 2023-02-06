from django.http import HttpResponse
from django.shortcuts import render

def hello(requst):
    return render(requst,'index.html')

def home(request):
   number1=int( request.GET['num1'])
   number2= int( request.GET['num2'])
   sum=number1+number2
   difference=number2-number1
   product=number1 * number2
   division=number2 / number1
   return render(request,'home.html',{'sum':sum,'diff':difference,'product':product,'div':division})

