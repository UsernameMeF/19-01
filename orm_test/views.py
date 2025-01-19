from django.shortcuts import render
from orm_test.models import Author, Post


# Create your views here.
def main(request):
    username = "Ім'я"
    return render(request, 'main_page.html', {"name": username})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_page.html', {"authors": authors})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_page.html', {"posts": posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", {"post": post})


def posts_by_author(request, author_id):
    author = Author.objects.get(id=author_id)

    if author:
        posts = Post.objects.filter(author=author)
    else:
        posts = []

    return render(request, "posts_by_author.html", {'author': author, 'posts': posts})