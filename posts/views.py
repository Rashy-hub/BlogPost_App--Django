from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post
from .forms import PostCreationForm


def posts_list(request):

    posts = Post.objects.all()

    author_id = request.GET.get("author")
    if author_id:
        posts = posts.filter(author_id=author_id)

    search_query = request.GET.get("search", "").strip()
    if search_query:
        posts = posts.filter(title__icontains=search_query)

    date_order = request.GET.get("date", "desc")
    if date_order == "asc":
        posts = posts.order_by("created_at")
    else:
        posts = posts.order_by("-created_at")

    authors = User.objects.filter(post__isnull=False).distinct()

    return render(
        request, "posts/posts_list.html", {"posts": posts, "authors": authors}
    )


def posts_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "posts/posts_page.html", {"post": post})


@login_required(login_url="/users/login/")
def posts_create(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("posts:page", slug=post.slug)
    else:
        form = PostCreationForm()

    return render(request, "posts/posts_create.html", {"form": form})
