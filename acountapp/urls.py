from django.urls import path
from acountapp.views import hello_world

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
