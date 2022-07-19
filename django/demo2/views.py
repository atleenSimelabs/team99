import datetime
from django.shortcuts import render

def index(request):
    now = datetime.datetime.now()
    return render(request, "demo2/index.html", {
        "demo2": now.month == 1 and now.day == 1
    })
