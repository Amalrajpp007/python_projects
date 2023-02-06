from django.urls import path

from mvapp import views
app_name='mvapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('movie/<int:id>/',views.details,name='details'),
    path('add',views.add_image,name='add_image'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]