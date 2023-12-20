from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "titulo",
            "descripcion",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Escribe el titulo"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Escribe la descripcion"}
            ),
        }
