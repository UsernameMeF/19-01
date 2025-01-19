import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post

Author.objects.create(first_name="Igor", last_name="Hoh", email="aaa@gmail.com")


#author = Author.objects.filter(first_name = "Igor").first()
#author.first_name = "Anton"
#author.save()
#print(author)

#post = Post.objects.create(title="Post 1", body="TEXT IN POST", author=author)

post = Post.objects.get(id=1)
# print(post)
# print(post.created_at)