from django.shortcuts import render
from projects.models import Project
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
