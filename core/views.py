from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, Comment, Event
from django.contrib.auth.models import User
from django.db.models import Count, Q


def index(request):
    return render(request, 'index.html')


def about(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'about.html', {'events': events})


@login_required
def dashboard(request):
    user = request.user
    if user.is_staff:
        users = User.objects.annotate(
            total_assigned=Count('assigned_tasks', distinct=True),
            completed_tasks=Count('assigned_tasks', filter=Q(assigned_tasks__completed=True), distinct=True)
        )
        # prepare task list and simple metrics
        tasks = Task.objects.all().order_by('-created_at')
        for u in users:
            total = u.total_assigned or 0
            done = u.completed_tasks or 0
            u.completion_rate = (done / total * 100) if total > 0 else 0
            context = {'admin': True, 'users': users, 'tasks': tasks}
    else:
        tasks = Task.objects.filter(assigned_to=user).order_by('-created_at')
        context = {'admin': False, 'tasks': tasks}
    return render(request, 'dashboard_new.html', context)


@login_required
def task_list(request):
    user = request.user
    if user.is_staff:
        tasks = Task.objects.all().order_by('-created_at')
    else:
        tasks = Task.objects.filter(assigned_to=user).order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(task=task, author=request.user, content=content)
            return redirect('task_detail', pk=pk)
    return render(request, 'task_detail.html', {'task': task})
