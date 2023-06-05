from django.shortcuts import render
from projects.models import Project
# Create your views here.

def List_Projects(request):
    list_projects = Project.objects.all()
    context = {
        "projects": list_projects,
    }

    return render(request, "projects/list_projects.html", context)
