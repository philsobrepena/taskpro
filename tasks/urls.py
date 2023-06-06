from django.urls import path
from tasks.views import Create_Task

urlpatterns = [
    path("create/", Create_Task, name="create_task"),
]
