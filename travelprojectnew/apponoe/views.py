from django.http import HttpResponse
from django.shortcuts import render

from apponoe.models import Place, Team


# Create your vieHome pagews here.
def home(requst):
    place=Place.objects.all()
    team=Team.objects.all()
    return render(requst,'index.html',{'places':place,'Team':team})