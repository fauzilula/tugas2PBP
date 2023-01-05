from django import forms
from todolist.models import Task

class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['user', 'date']#?