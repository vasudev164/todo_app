from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Todo


# Create your views here.
def show_todo_list(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)


def add_todo(request):
    if request.method == 'POST':
        if request.POST['name']:
            obj = Todo.objects.create(name=request.POST['name'])
            obj.save()
            return HttpResponseRedirect(reverse('todo:show_todo_list'))
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)


def delete_todo(request, pk):
    obj = Todo.objects.get(pk=pk)
    obj.delete()
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)
