from django.shortcuts import render , redirect
from . import views
from .models import Project, Task , SubTask
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .form import CreateProject, CreateTask , CreateSubtask
# Create your views here.


def view(request):
    view = Project.objects.all()
    return render(request, 'project/view.html', {'view': view})

def detail(request,pk):
    detail = Project.objects.get(id=pk)
    q = detail.project_name
    task = Task.objects.filter(project__project_name = q)
    context = {
        'detail': detail,
        'task': task
    }
    return render(request, 'project/detail.html', context)

def create(request):
    form = CreateProject()
    if request.method == 'POST':
        form = CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('view')
    return render(request, 'project/creates.html', {'form' : form})

def update(request,pk):
    up = Project.objects.get(id=pk)
    form = CreateProject(instance=up)
    if request.method == 'POST':
        form = CreateProject(request.POST, instance=up)
        if form.is_valid():
            form.save()
            return redirect('detail', pk)
    return render(request, 'project/creates.html', {'form': form})

def createtask(request,pk):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            ins= form.cleaned_data['task_name']
            i=Task.objects.get(id=id)
            tempalte = render_to_string('project/addtask.html', {'i':i})
            email = EmailMessage(
            'ADD Task',
            tempalte,
            settings.EMAIL_HOST_USER,
            ['djangotest05@gmail.com'],
            )
            email.fail_silently=False
            email.send()   
            return redirect ('detail',pk)
    return render(request, 'project/create_task.html', {'form' : form})

def updatetask(request,pk):
    i = Task.objects.get(id=pk)
    form = CreateTask(instance=i)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=i)
        if form.is_valid():
            form.save()
            return redirect('viewtask',pk)
    return render(request, 'project/create_task.html', {'form': form})

def viewtask(request,pk):
    task = Task.objects.get(id=pk)
    q = task.task_name
    sub = SubTask.objects.filter(task__task_name = q)
    context = {
        'task': task,
        'sub': sub
    }
    return render(request, 'project/view_task.html', context)

def createsubtask(request,pk):
    form = CreateSubtask()
    if request.method == 'POST':
        form = CreateSubtask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewtask', pk)
    return render(request, 'project/create_task.html', {'form' : form})

def viewsub(request,pk):
    i=SubTask.objects.get(id=pk)
    return render(request, 'project/view_sub.html', {'i':i})

def updatesubtask(request,pk):
    i= SubTask.objects.get(id=pk)
    form = CreateSubtask(instance=i)
    if request.method == 'POST':
        form = CreateSubtask(request.POST, instance=i)
        if form.is_valid():
            form.save()
            return redirect('viewsub', pk)
    return render(request, 'project/create_task.html', {'form' : form})