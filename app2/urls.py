from django.urls import path,include
from app2.views import *
app_name='something'

urlpatterns=[
    path('second/',second,name='second')
]