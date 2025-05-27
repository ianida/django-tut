from django import forms
from .models import Students

# This form is used to create and update student profiles

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'