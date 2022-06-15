from django.shortcuts import render
from .models import Todo
# Create your views here.

from django import forms


def index(request):
    return render(request, 'base/index.html')


# form
class todoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name', 'checked')


# get, post, delete, set
def todo1_get_and_post(request):
    todo_form = todoForm
    ctx = { 'todo_form' : todo_form}


    return render(request, 'todo1/index.html', ctx)

