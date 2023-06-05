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
