from django.urls import path
from .view_todo import todo_get_and_post

from .view_board import *

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="base/index.html"), name="index"),

    # Todo
    path('todo/', todo_get_and_post, name="todo"),

    # Board
    path('board/', board, name="board"),


    # Notes
    # path('notes/', notes, name="notes"),




]
