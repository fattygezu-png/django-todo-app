from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):  # or task_list, depending on your function name
    if not request.user.is_authenticated:
        return redirect('login')

    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')  # or your dashboard url name

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/home.html', context)