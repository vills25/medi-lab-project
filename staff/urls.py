from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
]


# Create your URLS here.
