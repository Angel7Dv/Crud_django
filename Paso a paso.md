
# wsl2 

instalaciones y comandos

wsl2 ubuntu



# Instalacion 




# Registro de las apps

## Creacion y configuraion del proyecto


- crear la tabla de tareas

```python
from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

```

- Realizar las migraciones
- crear superuusuario
- agrega el models al administrador

`admin.py`
```python
from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Task
# Register your models here.

admin.site.register(Task)

```


- Crear las views 

`task/views.py`
```python 
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!!")
    return render(request, "index.html") # add this line

```

- Modificar el static y plantillas


- Urls locales

`task/urls.py`
```python 
from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.index,name="index")
]
```


- Urls globales

`crud/urls.py`
```python 

from django.contrib import admin
from django.urls import path, include # add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task.urls'))  # add this line
]
```


- y pantillas 


# metodos Query



## POST

- Create new file

`forms.py`
```python
from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form

```



- lo importamos en la view.py


`view.py`
```python
from django.shortcuts import render, redirect
from .forms import TaskForm # lo importamos en la view.py

def index(request):
        form = TaskForm() # add this line


        if request.method == "POST": # objeto de solicitud y su parametro .method
                print("esto es request" , request )
                #Get the posted form
                form = TaskForm(request.POST)
                if form.is_valid():   
                        form.save()
                        return redirect("index")

        return render(request, "form.html", {"task_form": form})
```

todo sobre request y el objeto WSGIRequest  https://programmerclick.com/article/14281043097/


- 
`index.html`
```html

 <form method="post">
    {% csrf_token %}
        <!-- {{task_form}} to display all -->
        {{task_form.title}} <!-- to display particular field-->
        <button type="submit">SUBMIT</button>
    </form>


```

- personalizacion
    "de aqui en adelante index lo pase a una plantilla padre y el formulario lo deje en form.html, ademas agrege una plantilla home.html



# GET

- add to view 

`view.py`

```python
from .models import Task # Add for GET method
def form(request):
        form = TaskForm() 
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
```

- add to html

`form.html`
```html


            <!-- this changes -->
        <ol>
            {% for t in tasks_list %}
                <li>{{t.title}}  {{t.completed}}</li>
            {% endfor %}
        </ol>
```



# UPDATE

- Primero añadimos una Url que pasara el parametro de la id de la tarea 

`index.html`
```html


            <!-- this changes -->
        <ol>

            

            {% for t in tasks_list %}
                <li>{{t.title}} <a href="{% url "update_task" t.id %}">Update</a></li>
                                    <!-- crearemos esta url: parametro de objeto -->
            {% endfor %}
        </ol>
```


- añadimos la url "update_task"

`urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('form/',views.form, name="form"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
]
```

- añadimos la view


`view.py`

```python

def update_task(request, pk): # pk = parametro   t.id %}" en el link del html
    task = Task.objects.get(id=pk) # selecciona el objeto segun la id pasada por la url
    form = TaskForm(instance=task) # formulario asignado al objeto espesifico

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("form")

    return render(request, "update_task.html", {"task_edit_form": form})

```

- Creamos el html de update_task





- Agregar feeback al usuario


`form.html`

```html


<div class="card">
    <div class="card-body">
        <form method="post">
            {% csrf_token %} 
                <!-- {{task_form}} to display all -->
                {{task_form.title}} <!-- to display particular field-->
                <button type="submit">SUBMIT</button>
        </form>
        
    </div>
            <!-- this changes -->
        <ol>
            {% for t in tasks_list %}

            <li>

                {% if t.completed == True %}
                <strike>{{t.title}} </strike>
                {% else %}
                    {{t.title}}
                {% endif %}  
                <a class="btn" href="{% url "update_task" t.id %}">✒</a></li>
            {% endfor %}
        </ol>
</div>

```

# DELETE


- primero agrego la url para eliminar en el html


`form.html`
```html
<a href="{% url "delete_task" task.id %}">Delete❌</a>
    
```

- agregamos a las urls

`urls.py`

```python
 path("delete/<int:pk>/", views.delete_task, name="delete_task"),

```


- add to view.py

`view.py`

```python

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("form")
    
```



