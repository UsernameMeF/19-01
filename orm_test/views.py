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


