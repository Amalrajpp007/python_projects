from django.urls import path

from bkapp import views
app_name='bkapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('book/<int:b_id>/',views.details,name='details'),
    path('update/<int:b_id>/', views.update, name='update'),
    path('add', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),

]