from django.contrib import admin
from django.urls import path,include
from crudapp import views

urlpatterns = [
    path('',views.read,name='read'),
    path('insert/',views.insert,name='insert'),
    path('success/',views.success,name='success'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('contact/',views.contact,name='contact'),
    path('download/',views.download,name='download'),
    
    
]