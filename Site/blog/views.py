from django.shortcuts import render, get_list_or_404, redirect
from .models import Post, Comment
from datetime import datetime
# from .forms import CommentForm
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django import template


# Create your views here.


def pools(request):
    return HttpResponse("Hello")


def home_view(request):
    return HttpResponse("hi")


def index(request):
    try:
        posts = Post.objects.all()
    except ObjectDoesNotExist:
        raise Http404("Post does not exit!")

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list():
    pass


def post_details():
    pass


def post_comment():
    pass


def add_comment():
    pass
