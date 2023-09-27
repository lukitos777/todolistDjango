from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    tasks = task.objects.all()

    form = taskForm()

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, "form": form}
    return render(request, "tasks/list.html", context)


def updateTask(request, pk):
    task_ = task.objects.get(id=pk)

    form = taskForm(instance=task_)

    if request.method == 'POST':
        form = taskForm(request.POST, instance=task_)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    contenxt = {'item': item}
    return render(request, 'tasks/delite.html', contenxt)


