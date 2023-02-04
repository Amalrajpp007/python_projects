from django.urls import path

from todoapp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('delete/<int:t_id>/',views.delete, name='delete'),
    path('update/<int:t_id>/', views.update, name='update'),
    path('classlist', views.TodoListView.as_view(), name='classlist'),
    path('classupdate/<int:pk>/', views.TodoUpdateView.as_view(), name='classupdate'),
    path('classdelete/<int:pk>/', views.TodoDeleteView.as_view(), name='classdelete'),
    path('classdetails/<int:pk>/', views.TodoDetailsView.as_view(), name='classdetails'),

]