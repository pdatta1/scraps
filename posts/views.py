from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, ScrapUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from posts.create_post import CreatePostForm
from posts.create_user import CreateUserForm, EditUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse


@xframe_options_exempt
def create_user(request):
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, "Account Created.")
            return redirect('posts:index')
    else:
        register_form = CreateUserForm
    return render(request=request, template_name="posts/create_user.html", context={"register_form": register_form})


@xframe_options_exempt
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
@xframe_options_exempt
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("posts:index")


@login_required
@xframe_options_exempt
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
    return render(request=request, template_name="posts/create_post.html",
                  context={'post_form': post_form, })


@login_required
@xframe_options_exempt
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


def get_user_ip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)


@login_required
@xframe_options_exempt
def succeed_edit_post(request):
    return render(request=request, template_name='posts/succeed_edit_post.html')



def pump(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    pumped = False
    if post.pumps.filter(id=request.user.id).exists():
        post.pumps.remove(request.user)
        pumped = False
    else:
        post.pumps.add(request.user)
        pumped = True

    return HttpResponseRedirect(reverse('posts:post_detail', args=[str(pk)]))



class PostList(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = 'posts/index.html'
    queryset = Post.objects.filter(status=1,).order_by('-created_on')



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        data = get_object_or_404(Post, id=self.kwargs['pk'])
        pumped = False
        if data.pumps.filter(id=self.request.user.id).exists():
            pumped = True 
        
        context['pumped'] = pumped  
        return context 


def edit_profile(request):
    if request.method == 'POST':
        editform = EditUserForm(request.POST, instance=request.user)
        if editform.is_valid():
            editform.save()
            return redirect('posts:profile')
    else:
        editform = EditUserForm(instance=request.user)
    return render(request=request, template_name='posts/edit_profile.html', context={'form': editform})

def edit_profilepic(request):
    pass

class View_Profile(generic.DetailView):
    model = Post 
    template_name = 'posts/view_profile.html'



def delete_user(request):
    if request.method == 'POST':
        user = ScrapUser.objects.filter(username=request.user)
        user.delete()
        return redirect('posts:index')
    return render(request=request, template_name='posts/delete_user.html')


@xframe_options_exempt
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordResetForm(request.POST)
        if password_change_form.is_valid():
            data = password_change_form.cleaned_data['email']
            scrap_user = ScrapUser.objects.filter(Q(email=data))
            if scrap_user.exists():
                for user in scrap_user:
                    subject = 'Change Your Password'
                    email_template_name = 'posts/password_change/password_reset_email.txt'
                    content = {
                        'email': user.email,
                        'domain': 'https://www.scrapnc.com',
                        'site_name': 'ScrapSite',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    scrap_email = render_to_string(email_template_name, content)
                    try:
                        send_mail(subject, scrap_email, 'ncscrapsite@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        messages.error('Invalid Header Found')
                    logout(request)
                    return redirect('password_reset_done')
    password_change_form = PasswordResetForm()
    return render(request=request, template_name='posts/password_change/password_reset.html',
                  context={'password_change_form': password_change_form})
