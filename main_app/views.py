from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy # Easy redirection
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # Restricts users from accessing others' data
from django.contrib.auth.forms import UserCreationForm # Creates a user automatically
from django.contrib.auth import login # Logs the new user in automatically


# Create your views here.

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
######################################  

class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    # Triggers validation and submits UserCreationForm
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    # Redirect to tasks if already authenticated, otherwise back to Register
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register, self).get(*args, **kwargs)
    
###################################### 

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            
        context['search_input'] = search_input
        return context
    
######################################   

class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name ='task_details.html'
    context_object_name = 'task'
    
######################################

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    
    # Stops users from creating for other users
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
#######################################

class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

######################################
   
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')