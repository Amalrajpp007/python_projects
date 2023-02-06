from django.http import HttpResponse
from django.shortcuts import render, redirect

from mvapp.form import MovieForm
from mvapp.models import Movie


# Create your views here.
def home(request):
    movie=Movie.objects.all()
    return  render(request,'home.html',{'movies':movie})
def details(request,id):
   movie= Movie.objects.get(id=id)
   return render(request,'details.html',{'i':movie})

def add_image(request):

    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
