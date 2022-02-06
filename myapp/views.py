from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .models import ToDo, CompletedToDo
from datetime import date 

def home(request):
    todos = ToDo.objects.filter(is_active=True)
    new_list = []
    for todo in todos:
        is_completed_result = CompletedToDo.objects.filter(date=date.today(), todo=todo).first()
        if is_completed_result and is_completed_result.is_done:
            is_completed = True 
        else:
            is_completed = False 
        if(is_completed):
            new_list.append({'pk': todo.pk, 'title': todo.title, 'icon': todo.icon, 'url': todo.url, 'done': True})
        else:
            new_list.append({'pk': todo.pk, 'title': todo.title, 'icon': todo.icon, 'url': todo.url, 'done': False})
    return render(request, 'myapp/todo_list.html', context={'todo_list': new_list})



def mark_done(request, pk):
    
    todo = get_object_or_404(ToDo, pk=pk)

    completed_todo = CompletedToDo.objects.get_or_create(date=date.today(), todo=todo)[0]
    completed_todo.is_done = not completed_todo.is_done 
    completed_todo.save()
    return JsonResponse({"status": f"{completed_todo.is_done}"})
    

def mark_undone(request, pk):
    if request.method == 'POST':
        to_date = request.POST.get('date')
        todo = get_object_or_404(ToDo, pk=pk)

        completed_todo = CompletedToDo.objects.get_or_create(date=to_date, todo=todo)[0]
        completed_todo.is_done = True 
        completed_todo.save()
        return JsonResponse({"status": "success"})
    else:
        return HttpResponse("NOT Allowed")

        
def mark_inactive(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(ToDo, pk=pk)
        todo.is_active = False
        return JsonResponse({"status": "success"})
    else:
        return HttpResponse("NOT Allowed")


def mark_active(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(ToDo, pk=pk)
        todo.is_active = True
        return JsonResponse({"status": "success"})
    else:
        return HttpResponse("NOT Allowed")

def inactive_todos(request):
    todos = ToDo.objects.filter(is_active=False)
    return render(request, 'myapp/todo_list.html',context={'todo_list': todos})
    


