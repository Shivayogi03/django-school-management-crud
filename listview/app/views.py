from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView


class school_list(ListView):
    model=School
    context_object_name='QSLSO'
    