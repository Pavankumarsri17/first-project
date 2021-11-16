from typing import Pattern
from django.urls import path
from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls.resolvers import URLPattern
from app1.views import *
app_name='app1'
urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]