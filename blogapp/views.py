# from re import template
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment, Post
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator


def home(request):
    Post_list = Post.objects.all()
    paginator = Paginator(Post_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/home.html', {'page_obj': page_obj})


def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'home/detail.html', {'post': post})


def list(request):
    return render(request, 'home/list.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def userprofile(request):
    return render(request, 'home/userprofile.html')


def bloghome(request):
    Post_list = Post.objects.all()
    paginator = Paginator(Post_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/bloghome.html', {'page_obj': page_obj})


def thanks(request):
    return render(request, 'home/thanks.html')


def search(request):
    q = request.GET['q']
    allPosts = Post.objects.filter(title__icontains=q)
    params = {'allPosts': allPosts}
    return render(request, 'home/search.html', params)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/thanks"

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        initial = initial.copy()
        initial['author'] = self.request.user.pk
        return initial


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/thanks"


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:bloghome')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = "/thanks"

    def get_initial(self):
        initial = super(CommentCreateView, self).get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user.pk
        return initial
