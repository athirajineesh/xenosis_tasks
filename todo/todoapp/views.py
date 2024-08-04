from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

#listview:only these 4 lines needed to view our home page
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'name'#key we used in dictionary


def add(request):
    if request.method == 'POST':
        taskname = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(task=taskname, priority=priority, date=date)
        task.save()

    pending_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    return render(request, "home.html", {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    })



def delete(request,taskid):
    taskdelete=Task.objects.get(id=taskid)
    if request.method=='POST':
        taskdelete.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    taskupdate=Task.objects.get(id=id)
    fetch=todoform(request.POST or None,instance=taskupdate)
    if fetch.is_valid():
        fetch.save()
        return redirect('/')
    return render(request,"edit.html",{'f':fetch,'t':taskupdate})

def completed(request, taskid):
    taskdone = Task.objects.get(id=taskid)
    if request.method == 'POST':
        taskdone.is_completed = True
        taskdone.save()
        return redirect('/')
    return render(request, "done.html")


