from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class school_list(ListView):
    model=School
    context_object_name='QSLSO'

class school_detail(DetailView):
    model=School
    context_object_name='RSO'
    

class SchoolCreate(CreateView):
    model=School
    fields='__all__'
    template_name='app/school_form.html'


class Home(TemplateView):
    template_name='app/Home.html'


class schoolupdate(UpdateView):
    model=School
    fields='__all__'
    

class Deleteschool(DeleteView):
    model=School
    context_object_name='SCO'
    success_url=reverse_lazy('school_list')