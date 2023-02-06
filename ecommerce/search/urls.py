from django.urls import path

from search import views
app_name='search_app'
urlpatterns=[
    path('',views.searchProduct,name='searchProduct')
]