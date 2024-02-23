from django.shortcuts import render, redirect
from .models import UserTodo
from .forms import UserForm
from django.views.decorators.http import require_POST
# from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    form =UserForm()
    all_todos = UserTodo.objects.order_by('id')
    context ={"todos": all_todos, 'form': form}
    return render(request, 'index.html', context)

@require_POST
def add_forms(request):
    form = UserForm(request.POST)
    # print(request.POST['text'])
    if form.is_valid():
        new_todo = UserTodo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def complete(request, todo_id):
    todo = UserTodo.objects.get(pk=todo_id)
    todo.status = True
    todo.save()

    return redirect('index')

def delete_complete(request):
    UserTodo.objects.filter(status__exact=True).delete()

    return redirect('index')

def deleteall(request):
    UserTodo.objects.all().delete()

    return redirect('index')