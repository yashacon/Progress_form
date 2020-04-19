from django.urls import path

from . import views

urlpatterns=[
    path('',views.Submit,name='Submit'),
    path('list',views.List,name='List'),
    ]
