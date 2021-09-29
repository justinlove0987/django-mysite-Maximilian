from datetime import date

from django.shortcuts import render

from .models import Post

all_posts = [


]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    # -date means order by descending order, to make sure the post we added the last is on top.
    # Django will convert this all statement into SQL command. 'Post.objects.all().order_by("-date")[:3]'
    # 'Post.objects.all().order_by("-date")[-3:]' Django does not support negative index here!!!
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
