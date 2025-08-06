from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
# views.py
from django.http import HttpResponse, Http404, FileResponse, HttpResponseForbidden
from django.conf import settings
import os

@login_required
def serve_protected_image(request, filename):
    try:
        tweet = get_object_or_404(Tweet, photo=filename)
    except:
        # File doesn't exist in database
        raise Http404("Image not found")

    if tweet.is_private and tweet.user != request.user:
        # Use custom 403 handler by calling it directly
        return custom_403_view(request)

    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), content_type='image/jpeg')
    else:
        raise Http404("Image file not found on server")

def tweet_list(request):
    if request.user.is_authenticated:
        tweets = Tweet.objects.filter(
            Q(is_private=False) | Q(user=request.user)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.filter(is_private=False).order_by('-created_at')

    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Check if user can view this tweet
    if tweet.is_private and tweet.user != request.user:
        # If user is not authenticated, suggest login with 404
        if not request.user.is_authenticated:
            raise Http404("Post not found")
        else:
            # If user is authenticated but doesn't have access, show custom 403
            return custom_403_view(request)
    
    return render(request, 'tweet/tweet_detail.html', {'tweet': tweet})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet:tweet_list')
        else:
            return render(request, 'tweet/tweet_form.html', {'form': form})
    else:
        form = TweetForm()
        return render(request, 'tweet/tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet:tweet_list')
        else: 
            return render(request, 'tweet/tweet_form.html', {'form': form})
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form': form})
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet:tweet_list')
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('tweet:tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tweet:tweet_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('tweet:tweet_list')


# Custom Error Handlers
def custom_404_view(request, exception=None):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)


def custom_403_view(request, exception=None):
    """Custom 403 error page"""
    return render(request, '403.html', status=403)


def custom_500_view(request):
    """Custom 500 error page"""
    return render(request, '500.html', status=500)