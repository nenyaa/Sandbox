# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import BlogPost
from .forms import ContactForm, BlogPostModelForm
from .models import BlogPost


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to Try Django", "blog_list": qs}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About us"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact us", "form": form}
    return render(request, "form.html", context)


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "form.html"
    context = {"form": form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)
