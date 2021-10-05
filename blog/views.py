from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView

from .models import Post


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


class SinglePostView(DeleteView):
      template_name = "blog/post-detail.html"
      model = Post
      context_object_name = "post"

      def get_context_data(self, **kwargs):
          cotext = super().get_context_data(**kwargs)
          cotext["post_tags"] = self.object.tags.all()
          return cotext
