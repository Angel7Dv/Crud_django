from django.shortcuts import render
from .models import Task
from .forms import FormTask
# Create your views here.



# get, post, delete, set
def todo_get_and_post(request):
    form_task = FormTask
    ctx = { 'form_task' : form_task}


    return render(request, 'todo/index.html', ctx)

