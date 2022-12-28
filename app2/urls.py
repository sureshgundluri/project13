from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('gopi/',gopi,name='gopi'),
    path('madhu/',madhu,name='madhu')
]