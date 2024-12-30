from django.urls import path
from blog_project import views
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.posts_list, name="list"),
    path("create/", views.posts_create, name="create"),
    path("<slug:slug>", views.posts_page, name="page"),
]
