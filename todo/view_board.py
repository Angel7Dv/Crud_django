from django.shortcuts import render
from .models import Task, List
from .forms import FormTask, FormList


"""clone trello use Form + url + Methods tags + jQuery"""
def board(request):
    # GET
    list_task = Task.objects.all()
    
    # POST
    form_task = FormTask
    form_list = FormList


    # SET

    # DELET

    ctx = {
        'list_task':list_task,
        'form_task':form_task,
        'form_list':form_list,
    }

    return render(request, 'board/board.html', ctx)