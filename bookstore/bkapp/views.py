from django.http import HttpResponse
from django.shortcuts import render, redirect

from bkapp.forms import BookForm
from bkapp.models import Book


# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request,'home.html',{'books':books})

def details(request,b_id):
    book=Book.objects.get(id=b_id)
    return render(request,'details.html',{'books':book})
def update(request,b_id):
    book=Book.objects.get(id=b_id)
    form=BookForm(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'book':book})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author = request.POST.get('author')
        desc = request.POST.get('desc')
        img=request.FILES['img']
        book=Book(name=name,desc=desc,img=img,author=author)
        book.save()
        return redirect('/')
    return render(request,'add.html')
def delete(request,id):
    if request.method=='POST':

      book=Book.objects.get(id=id)
      book.delete()
      return redirect ('/')
    return render(request,'delete.html')