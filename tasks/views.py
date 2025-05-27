
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    status = request.GET.get('status')
    if status == 'completed':
        tasks = Tasks.objects.filter(completed=True)
    elif status == 'pending':
        tasks = Tasks.objects.filter(completed=False)
    else:
        tasks = Tasks.objects.all()

    return render(request, 'tasks/index.html', {'form': form, 'tasks': tasks})

def complete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('index')