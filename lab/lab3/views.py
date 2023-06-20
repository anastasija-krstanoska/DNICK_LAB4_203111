# from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from .models import Post, BlogUser, Block
from .forms import PostForm, BlockForm


# Create your views here.
def posts(request):
    qs = Post.objects.filter().all()
    print(qs)
    context = {"posts": qs}
    return render(request, "posts.html", context=context)


def addnew(request):
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            usr = BlogUser.objects.filter(user=request.user).get()
            post.user = usr
            # post.cover_image = form.cleaned_data['file']
            post.save()
            return redirect("/posts/")
    return render(request, "addnewpost.html", context={"form": PostForm})


def profile(request):
    user = BlogUser.objects.get(user=request.user)
    posts = Post.objects.filter(user=user)

    return render(request, "profile.html", {"user": user, "posts": posts})


def blocked(request: WSGIRequest):
    if request.method == "POST":
        form_data = BlockForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            block = form_data.save(commit=False)
            block.blocker = BlogUser.objects.get(user=request.user)
            block.save()

            return redirect("blocked")

    blocks = Block.objects.filter(blocker__user=request.user)
    blocked_users = BlogUser.objects.filter(user__in=blocks.values_list("blocked__user", flat=True))

    return render(request, "blockedUsers.html", {"form": BlockForm, "users": blocked_users})
