
from django.urls import path
from . import views
urlpatterns = [

    path('',views.creg,name='creg'),
    path('ar',views.areg,name='creg'),
    path('log',views.log,name='log'),



]
