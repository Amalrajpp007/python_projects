from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView

from todoapp.form import TodoForm
from todoapp.models import Todo


# Create your views here.
def home(request):
    task = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        todo = Todo(name=name, priority=priority, date=date)
        todo.save()
    return render(request, 'home.html', {'task': task})


def delete(request, t_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=t_id)
        todo.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, t_id):
    todo = Todo.objects.get(id=t_id)
    form = TodoForm(request.POST or None, request.FILES, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'todo': todo})


class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'task'


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']
    success_url = reverse_lazy('classlist')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('classlist')
class TodoDetailsView(DetailView):
    model = Todo
    template_name = 'details.html'
    context_object_name = 'task'

