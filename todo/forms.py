from django import forms
from .models import Task, List
# form


class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class FormList(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'