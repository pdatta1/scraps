from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, ScrapUser
from django.shortcuts import render, redirect
from posts.create_post import CreatePostForm
from posts.create_user import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse


def create_user(request):
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, "Account Created.")
            return redirect('posts:index')
    else:
        register_form = CreateUserForm
    return render(request=request, template_name="posts/create_user.html", context={"register_form": register_form})


def login_user(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("posts:index")
            else:
                messages.error(request, "Invalid username and password")
        else:
            messages.error(request, "Invalid username and password")
    login_form = AuthenticationForm()
    return render(request=request, template_name="posts/login_user.html", context={"login_form": login_form})


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("posts:index")


@login_required
def create_post(request):

    if request.method == 'POST':
        post_form = CreatePostForm(request.POST, request.FILES)

        if post_form.is_valid():
            fs = post_form.save(commit=False)
            fs.author = request.user
            fs.save()
            messages.success(request, "Post Created.")
            return redirect("posts:index")
        else:
            print(post_form.errors)
    else:
        post_form = CreatePostForm()
    return render(request=request,template_name="posts/create_post.html",
                  context={'post_form': post_form,})


@login_required
def my_profile(request):
    logged_in_user = request.user
    page = request.GET.get('page', 1)
    my_posts = Post.objects.filter(author=logged_in_user)
    paginator = Paginator(my_posts, 5)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request=request, template_name='posts/my_profile.html', context={"my_posts": pages})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/edit_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'

    def get_success_url(self, **kwargs):
        return reverse('posts:profile')


@login_required
def succeed_edit_post(request):
    return render(request=request, template_name='posts/succeed_edit_post.html')


class PostList(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/index.html'

    queryset = Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
