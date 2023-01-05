import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from todolist.forms import *
from django.core import serializers
from django.shortcuts import render
from todolist.models import Task
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required(login_url='/todolist/login')
def show_todolist(request):
    todo=Task.objects.filter(user=request.user)
    context={
        'username':request.user.username,
        'list_todo':todo
    }
    return render(request,"todolist.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('user_name', username)
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login')
def addtodo(request):
    form = AddTaskForm()
    context = {'form': form,}
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.user = request.user
            saved.save()

            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            form = AddTaskForm()
            return redirect('todolist:addtask')

    return render(request, 'addtodo.html', context)

def updated(request, id):
    task = Task.objects.get(pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

def deleted(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_json(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(
            title = title, 
            description = description,
            date = datetime.date.today(), 
            is_finished = False, 
            user=request.user
            )

        result = {
            'id':task.id,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            }
        }
        return JsonResponse(result)
