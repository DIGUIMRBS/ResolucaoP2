from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Todo

class TodoListView(ListView):
 model = Todo