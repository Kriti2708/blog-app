import email
from email import message
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment, Post, Profile
from .forms import PostForm, CommentForm, ProfileForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
# from django.contrib import messages
# # from django.contrib.auth.decorators import login_required
# from operator import is_not
# from django.http import HttpResponseRedirect


def home(request):
    Post_list = Post.objects.all()
    paginator = Paginator(Post_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/home.html', {'page_obj': page_obj})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = "/thanks"

    def get_initial(self):
        initial = super(PostCreateView, self).get_initial()
        initial = initial.copy()
        initial['author'] = self.request.user.pk
        return initial


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blogapp/post_form.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    success_url = "/thanks"


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = "blogapp/comment.html"
    model = Comment
    form_class = CommentForm

    def get_initial(self):
        initial = super(CommentCreateView, self).get_initial()
        initial = initial.copy()
        initial['user'] = self.request.user.pk
        initial['post'] = self.kwargs['pk']
        return initial

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['comments'] = self.model.objects.filter(post_id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('blogapp:comment', kwargs={'pk': self.kwargs['pk']})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('blogapp:comment', kwargs={'pk': self.kwargs['post_id']})

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "blogapp/profile_form.html"
    success_url = reverse_lazy('blogapp:userdashboard')


def profile(request):
    return render(request, 'home/profile.html')


def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'home/detail.html', {'post': post})


def signup(request):
    return render(request, 'home/signup.html')


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'subject ',
            'test',
            'baghelkriti@gmail.com', #from
            ['admin@gmail.com'], #to 
            fail_silently=False,
        )
    return render(request, 'home/contact.html')


def userdashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
        return render(request, 'home/userdashboard.html', {'posts': posts})


def search(request):
    q = request.GET['q']
    allPosts = Post.objects.filter(title__icontains=q)
    params = {'allPosts': allPosts}
    return render(request, 'home/search.html', params)


def thanks(request):
    return render(request, 'home/thanks.html')
