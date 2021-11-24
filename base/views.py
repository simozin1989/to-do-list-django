from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from .models import Task

from django.urls import reverse_lazy

# Create your views here.


class CustomloginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
        

    


class TaskList(ListView):

    mode = Task
    context_object_name = 'list_task'

    def get_queryset(self):
        return Task.objects.all()


class TaskDetail(DetailView):
    mode = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

    def get_queryset(self):
        return Task.objects.all()


class TaskCreate(CreateView):
    mode = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    template_name = 'base/task_form.html'

    def get_queryset(self):
        return Task.objects.all()




class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
    def get_queryset(self):
        return Task.objects.all()
    
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
        

