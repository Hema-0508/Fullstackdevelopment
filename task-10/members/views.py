from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Member, Todo


# Existing main page
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))


# Display all members
def members(request):
    mymembers = Member.objects.all().values()

    template = loader.get_template('all_members.html')

    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


# Member details
def details(request, id):
    mymember = Member.objects.get(id=id)

    template = loader.get_template('details.html')

    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))


# -------------------------
# TODO CRUD
# -------------------------

# CREATE + READ
def todo(request):

    if request.method == "POST":

        task = request.POST.get("task")

        if task:
            Todo.objects.create(task=task)

    todos = Todo.objects.all()

    return render(request, "todo.html", {
        "todos": todos
    })


# UPDATE
def update_todo(request, id):

    todo = Todo.objects.get(id=id)

    if request.method == "POST":

        todo.task = request.POST.get("task")
        todo.save()

        return redirect("todo")

    return render(request, "update_todo.html", {
        "todo": todo
    })


# DELETE
def delete_todo(request, id):

    todo = Todo.objects.get(id=id)

    todo.delete()

    return redirect("todo")