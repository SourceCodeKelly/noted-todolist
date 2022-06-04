from asyncio import tasks
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
#For restricting users:
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name ='task_details.html'
    context_object_name = 'task'
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')