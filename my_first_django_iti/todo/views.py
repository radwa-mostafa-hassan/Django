from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import HttpResponseRedirect
my_todos = {
    1: {'task': 'reading', 'priority': 1, 'time': '30 mins', 'is_finished': "In progress"},
    2: {'task': 'Fitness', 'priority': 2, 'time': '30 mins', 'is_finished': "In progress"},
    3: {'task': 'Learning', 'priority': 3, 'time': '2 hours', 'is_finished': "In progress"},
}


def show_todo(request):
    return render(request, 'todo/todo.html', context={'todo_list': my_todos})


def delete_task(request, **kwargs):
    target_task = kwargs.get('task_id')
    my_todos.pop(target_task)
    return redirect(reverse('todo:home'))


def mark_as_done(request, **kwargs):
    target_task = kwargs.get('task_id')
    make_done = my_todos.get(target_task)
    make_done['is_finished'] = 'Done'
    return redirect(reverse('todo:home'))


def show_task(request, **kwargs):
    target_task = kwargs.get('task_id')
    details = my_todos.get(target_task)
    return render(request, 'todo/details.html', context={'details': details, 'task_no': target_task})


def add_task(request):
    new_task = request.POST['new_task']
    my_todos[4] = {}
    my_todos[4]['task'] = new_task
    my_todos[4]['time'] = '2 hours'
    my_todos[4]['priority'] = 5
    my_todos[4]['is_finished'] = "in progress"
    return redirect(reverse('todo:home'))


def edit_task(request, **kwargs):
    target_task = kwargs.get('task_id')
    details = my_todos.get(target_task)
    return render(request, 'todo/edit.html', context={'details': details, 'task_no': target_task})


def update_task(request, **kwargs):
    target_task = kwargs.get('task_id')
    task = request.POST['task']
    my_todos[target_task]['task'] = task
    return redirect(reverse('todo:home'))
