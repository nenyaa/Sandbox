from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.


def list(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.order_by('-created_at')
    return render(request, 'posts/list.html', {"posts_list": posts_list})


def add(request):
    if request.method == "POST":
        ob = PostForm(request.POST)
        ob.save()
        return redirect('posts_list')
    else:
        ob = PostForm()
        return render(request, 'posts/add.html', {"form": ob})


def details(request, id):
    ob = Post.objects.get(pk=id)
    return render(request, 'posts/details.html', {"details": ob})


def delete(request, id):
    Post.objects.filter(pk=id).delete()
    return redirect('posts_list')


def edit(request, id):
    ob = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        ob = PostForm(request.POST, instance=ob)
        ob.save()
        return redirect('posts_list')
    else:
        ob = PostForm(instance=ob)
        return render(request, 'posts/edit.html', {"form": ob})
