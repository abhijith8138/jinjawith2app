from abhi1.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('sample1/',sample1,name='sample1'),
]