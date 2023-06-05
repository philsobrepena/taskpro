from django.urls import path
from projects.views import List_Projects

urlpatterns = [
    path("", List_Projects, name="list_projects"),
]
