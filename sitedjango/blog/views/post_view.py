from django.http import HttpResponse
from django.views import generic

from django.shortcuts import render

from blog.models import Post


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
