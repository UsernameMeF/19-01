from django.urls import path

from orm_test import views


app_name = "main"

urlpatterns = [
    path('', views.main),
    path('posts/<int:post_id>/', views.post_detail, name="post_detail"),
    path('authors/', views.authors_list, name="authors"),
    path('posts/', views.posts_list, name="posts_list"),
    path('authors/<int:author_id>/posts/', views.posts_by_author, name="posts_by_author"),
]

