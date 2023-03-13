from abhi2.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('sample2/',sample2,name='sample2'),
]