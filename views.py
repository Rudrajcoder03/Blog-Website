from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(user=request.user, content=content)
        return redirect('home')
    
    return redirect('home')
    quit
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')
@login_required
def profile(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'posts': posts})

@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)

    if request.method == 'POST':
        post.content = request.POST.get('content')
        post.save()
        return redirect('profile')

    return render(request, 'update_post.html', {'post': post})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    return redirect('profile')

@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        profile.bio = request.POST.get('bio')

        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        return redirect('profile')

    return render(request, 'update_profile.html', {'profile': profile})

@login_required
def dashboard(request):
    user = request.user

    total_posts = Post.objects.filter(user=user).count()
    total_likes = sum(post.likes.count() for post in Post.objects.filter(user=user))
    followers = user.profile.followers.count()

    return render(request, 'dashboard.html', {
        'total_posts': total_posts,
        'total_likes': total_likes,
        'followers': followers
    })