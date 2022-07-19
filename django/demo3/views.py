from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

#third method
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

tasks = ["foo", "bar", "baz"]

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "demo3/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("demo3:index"))
        else:
            return render(request, "demo3/add.html", {
                "form": form
            })
    return render(request, "demo3/add.html", {
        "form": NewTaskForm()
    })

#second method
# def index(request):
#     return render(request, "demo3/index.html", {
#         "tasks": tasks
#     })

# def add(request):
#     if request.method == "POST":
#         form = NewTaskForm(request.POST)
#         if form.is_valid():
#             task = form.cleaned_data["task"]
#             tasks.append(task)
#             return HttpResponseRedirect(reverse("demo3:index"))
#         else:
#             return render(request, "demo3/add.html", {
#                 "form": form
#             })
#     return render(request, "demo3/add.html", {
#         "form": NewTaskForm()
#     })

#first method
# def index(request):
#     return render(request, "demo3/index.html", {
#         "tasks": tasks
#     })

# def add(request):
#     return render(request, "demo3/add.html")