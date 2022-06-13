from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from . models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('task_list') 
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_update.html'
    success_url = reverse_lazy('task_list') 
    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('task_list')
    
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'base/login.html'
    success_url = reverse_lazy('task_list')
    
     
    