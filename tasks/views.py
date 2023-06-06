from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Create_Task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)


@login_required
def Show_My_Tasks(request):
    show_my_tasks = Task.objects.filter(assignee=request.user)

    context = {
        "show_my_tasks": show_my_tasks,
    }

    return render(request, "mine/show_my_tasks.html", context)
