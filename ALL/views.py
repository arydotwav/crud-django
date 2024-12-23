from django.shortcuts import render
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm


def home(request):
    if request.user.is_authenticated:
        task = Task.objects.filter(user=request.user)
        return render(request, 'home.html', {
            'tasks': task
        })
    else:
        return render(request, 'home.html')

def sign_up(request):
    error = None
    if request.method == 'GET':
        return render(request, 'user/sign_up.html', {
        "form": CustomUserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render (request, 'home.html', {'show_alert': True})
            except:
                return render(request, 'user/sign_up.html', {
                    'form': CustomUserCreationForm,
                    'error': 'Username already exists!'
                })
        return render(request, 'user/sign_up.html', {
        "form": CustomUserCreationForm,
        'error': 'Passwords do not match! Try again!'
    })
    
def signin(request):
    error = None
    if request.method == 'GET':
        return render (request, 'user/log_in.html', {
            'form': CustomLoginForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render (request, 'user/log_in.html', {
                'form': CustomLoginForm,
                'error': 'Username or password incorrect!'
            })
        else:
            login(request, user)
            return redirect ('home')
 
def signout(request):
    logout(request)
    return redirect ('home')
    
@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/create.html', {
        'form': form
    })

@login_required
def editTask(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'tasks/edit_task.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('home')
        except:
            return render(request, 'tasks/edit_task.html', {'task': task, 'form': form, 'error': 'There was an error updating task. Please, try again!'})
    
def completedTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.completed = timezone.now()
        task.save()
        return redirect('showTasks')
    

def showTasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render (request, 'tasks/all.html', {
        'tasks': tasks
    })

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    return render(request, "tasks/task.html", {
        "task": task,
    })

def deleteTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        if request.POST.get('delete'):
            task.delete()
            return redirect('home')
        
    return redirect('home')