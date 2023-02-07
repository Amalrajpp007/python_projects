from django.urls import path

from apponoe import views

urlpatterns =[
    path ('', views.home,name='home'),
]
