from django.shortcuts import render
from django.utils import timezone
from blog.forms import CommentForm
from blog.models import Post, Comment, Category, Adminpost, User
import datetime
from django.http import HttpResponse
import os

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    admin = Adminpost.objects.all().order_by("-created_on")
    post = Post.objects.all()
    categories = Category.objects.all()
    user = User.objects.all()
    year = datetime.date.today().year
    BASE_DIR = "http://localhost:8000/tea_media/media/"
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

    context = {"posts": posts,  "categories": categories, "yearr": year, "admin":admin, "user": user,'pic': BASE_DIR}
    return render(request, "blog/blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    year = datetime.date.today().year
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/blog_detail.html", context)


