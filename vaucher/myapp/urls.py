# myapp/urls.py
from django.urls import path
from .views import home, my_view

urlpatterns = [
    path('', home, name='home'),
    path('myapp/', my_view, name='my_view'),
]
