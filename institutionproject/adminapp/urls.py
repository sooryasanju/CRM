from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_home.as_view(),name='home')
]