from django.urls import path
from tasks.views import Create_Task, Show_My_Tasks

urlpatterns = [
    path("mine/", Show_My_Tasks, name="show_my_tasks"),
    path("create/", Create_Task, name="create_task"),
]
