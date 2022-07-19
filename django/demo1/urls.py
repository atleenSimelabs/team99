from django.urls import path
from . import views

app_name="demo1"
urlpatterns = [
    path("", views.index, name="index"),
    path("hi", views.index2, name="index2"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
    # path("<str:name>", views.greet, name="greet"),
    path("<str:name1>", views.greet1, name="greet1")
    ]
