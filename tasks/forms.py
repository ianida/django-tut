from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['tasktitle','taskdescription','deadline'] #makes  models to forms from tasks

