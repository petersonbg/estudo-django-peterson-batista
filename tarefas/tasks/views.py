from turtle import done, title
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
from .forms import FormTask
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

@login_required
def taskList(request):

    search = request.GET.get('search')

    if search:

        tasks = Task.objects.filter(title__icontains=search)

    else:

        tasks_list = Task.objects.all().order_by('-created_at')

        paginator = Paginator(tasks_list, 3)
        
        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks':tasks})

@login_required
def taskView(request, id):
    task_task = get_object_or_404(Task, pk=id)
    show_task = {'task_task': task_task}
    return render(request, 'tasks/task.html', show_task)

@login_required
def newTask(request):
    if request.method == 'POST':
        form = FormTask(request.POST)

        if form.is_valid():
            task=form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')

    else:    
        form = FormTask
        return render(request, 'tasks/addtask.html', {'form':form})

@login_required   
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = FormTask(instance=task)

    if request.method == 'POST':
        form = FormTask(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return(redirect('/'))
        else:
            return render(request, 'tasks/edittask.html', {'form':form})

    else:
        return render(request, 'tasks/edittask.html', {'form':form})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso')
    return(redirect('/'))

@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if task.done == 'doing':
        task.done = 'done'
    
    else:
        task.done = 'doing'

    task.save()
    return redirect('/')

