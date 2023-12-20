from django.urls import path
from .views import list_task, create_task, delete_task

urlpatterns = [
    path("", list_task, name="tasks"),
    path("new/", create_task, name="new_task"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
]
