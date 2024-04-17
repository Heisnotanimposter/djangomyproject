from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('rsp', views.rsp, name='rsp'),
    path('context_django', views.context_django, name='context_django')
]
