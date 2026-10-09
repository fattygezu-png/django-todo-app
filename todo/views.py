from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/home.html', context)

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')