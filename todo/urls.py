from django.urls import path
from .views import index, todo1_get_and_post

urlpatterns = [
    path('', index, name="index"),

    #todo1
    path('todo1', todo1_get_and_post, name="todo1")

]
