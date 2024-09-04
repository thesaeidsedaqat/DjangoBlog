from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import PostForm
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_single.html'


class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'date', 'photo']
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
