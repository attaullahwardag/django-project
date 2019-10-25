from django.urls import path
from todoapp.views import postdata
from todoapp import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('post',postdata, name='post'),
]