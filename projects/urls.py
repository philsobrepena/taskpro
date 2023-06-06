from django.urls import path
from projects.views import List_Projects, Show_Project

urlpatterns = [
    path("<int:id>/", Show_Project, name="show_project"),
    path("", List_Projects, name="list_projects"),
]
