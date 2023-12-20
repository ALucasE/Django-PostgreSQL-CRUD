from django.shortcuts import get_object_or_404, render, redirect
from .models import Task


# Create your views here.
def list_task(request):
    tareas = Task.objects.all()
    return render(
        request,
        "lista_tareas.html",
        {
            "tareas": tareas,
        },
    )


def create_task(request):
    print(request.POST)
    nueva_tarea = Task(
        titulo=request.POST["titulo"], descripcion=request.POST["descripcion"]
    )
    nueva_tarea.save()
    return redirect("/tasks/")


def delete_task(request, task_id):
    tarea = Task.objects.get(id=task_id)
    tarea.delete()
    return redirect("/tasks/")
