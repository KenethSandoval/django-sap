from django.urls import path
from core.webapp.views import *

urlpatterns = [
    path('webapp/', index)    
]
