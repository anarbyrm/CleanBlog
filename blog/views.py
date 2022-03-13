from django.urls import reverse_lazy
from django.views.generic import (ListView,
 DetailView, 
 TemplateView, 
 CreateView, 
 UpdateView, 
 DeleteView)

from .models import Post

class IndexPage(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 1


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class AboutPage(TemplateView):
    template_name = 'about.html'


class CreatePost(CreateView):
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post'
    fields = ['title', 'subtitle', 'content', 'author']
    success_url = reverse_lazy('index')


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'subtitle', 'content']
    success_url = reverse_lazy('index')


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')




    

