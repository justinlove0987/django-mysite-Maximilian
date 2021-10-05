from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import Comment, CommentForm


class StartingPageView(ListView):
      template_name = "blog/index.html"
      model = Post
      context_object_name = "posts"
      ordering = ["-date"]

      def get_queryset(self):
          queryset =  super().get_queryset()
          data = queryset[:3]
          return data


class AllPostsView(ListView):
      template_name = "blog/all-posts.html"
      model = Post
      ordering = ["-date"]
      context_object_name = "all_posts"


class SinglePostView(View):
      def get(self, request, slug):
            post = Post.objects.get(slug=slug)
            context = {
                  "post": post,
                  "post_tages": post.tags.all(),
                  "comment_form": CommentForm()
            }
            return render(request, "blog/post-detail.html", context)

      # because slug is a part of the url for which this view is reached.
      # the slug parameter are passed by <slug:slug>, we set in urls.py
      def post(self, request, slug):
            comment_form = CommentForm(request.POST)
            post = Post.objects.get(slug=slug)

            if comment_form.is_valid():
                  # commit=False will not hit the database, but instead create a new model instance.
                  comment = comment_form.save(commit=False)
                  comment.post = post
                  comment.save()
                  return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
            
            context = {
                  "post": post,
                  "post_tages": post.tags.all(),
                  "comment_form": comment_form
            }
            return render(request, "blog/post-detail.html", context)