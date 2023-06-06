from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def List_Projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": list_projects,
    }

    return render(request, "projects/list_projects.html", context)

@login_required
def Show_Project(request, id):
    show_project = Project.objects.get(id=id)
    context = {
        "show_project": show_project,
    }
    return render(request, "projects/show_project.html", context)


@login_required
def Create_Project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_project.html", context)
