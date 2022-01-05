from django.shortcuts import render, redirect
from .forms import TaskForm # lo importamos en la view.py
from .models import Task # Add for GET method



def home(request):
        return render(request, "home.html")





def form(request):
        form = TaskForm() # add this line

        # POST

        if request.method == "POST": # objeto de solicitud y su parametro .method
                print("esto es request" , request )
                #Get the posted form
                form = TaskForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect("form")

        #GET 
        tasks = Task.objects.all() # add this for GET method
        print("lista de objetos" , tasks)

        return render(request, "form.html", {"task_form": form,  "tasks_list": tasks})


# UPDATE

def update_task(request, pk): # pk = parametro   t.id %}" en el link del html
    task = Task.objects.get(id=pk) # selecciona el objeto segun la id pasada por la url
    form = TaskForm(instance=task) # formulario asignado al objeto espesifico

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("form")

    return render(request, "update_task.html", {"task_edit_form": form})



# DELETE

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("form")