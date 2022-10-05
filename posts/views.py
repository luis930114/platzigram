""" Posts views. """

# Django
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 

#Forms
from posts.forms import PostForm
# Utilities
from datetime import datetime

#Models 
from posts.models import Post





"""def list_posts(request):
     List existing posts.
    content = []
    for post in posts:
        content.append(
            <p><strong>{name}</strong></p>
            <p><small>{user}- <i>{timestamp}</i></small></p>
            <figure><img src="{picture}" /></figure>
        .format(**post))
    return HttpResponse('<br>'.join(content))"""



"""@login_required
def list_posts(request):
    List existing posts
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})
"""


class PostsDetailView(LoginRequiredMixin, DetailView):
    """ Return posts detail view.  """
    template_name = 'posts/detail.html'
    model = Post
    queryset = Post.objects.all()
    slug_field = 'pk'
    slug_url_kwarg = 'post_id'
    context_object_name = 'post'


class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new Post. """

    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """ Add user and profile to context. """

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

"""@login_required
def create_post(request):
    Create new post view.
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )"""