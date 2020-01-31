from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Article
from .forms import UserRegistrationForm, UserLoginForm, ArticleForm


def home(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('article:dashboard')
        return render(request, 'index.html')


def usersignup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully')
            return redirect('article:login')
    else:
        if request.user.is_authenticated:
            return redirect('article:dashboard')
        form = UserRegistrationForm()
    return render(request, 'registration.html', {
        'form': form
    })


def usersignin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request, "Username or Password Incorrect")
                return redirect('article:login')
            else:
                login(request, user)
                return redirect('article:dashboard')
    else:
        if request.user.is_authenticated:
            return redirect('article:dashboard')
        form = UserLoginForm()
    return render(request, 'login.html', {
        'form': form
    })


@login_required(login_url=reverse_lazy('article:login'))
def usersignout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('article:login')


@login_required(login_url=reverse_lazy('article:login'))
def dashboard(request):
    if request.method == 'GET':
        articles = Article.objects.filter(user=request.user.pk).order_by('-pk')
        return render(request, 'dashboard.html', {
            'articles': articles
        })


@login_required(login_url=reverse_lazy('article:login'))
def postArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(False)
            article.user = request.user
            form.save()
            return redirect('article:dashboard')
    else:
        form = ArticleForm
    return render(request, 'createArticle.html', {
        'form': form
    })


def showArticles(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=request.GET['username'])
            articles = Article.objects.filter(user=user.pk, is_private=False)
            return render(request, 'showArticles.html', {
                'articles': articles or None
            })
        except User.DoesNotExist:
            messages.error(request, "Oops User does not exists")
            return render(request, 'showArticles.html')
