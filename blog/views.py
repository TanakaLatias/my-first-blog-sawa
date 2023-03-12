from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
#--
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
#--
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts' #Post.objects.all()
    model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

class PostCreateView(CreateView):
    template_name = 'blog/post_edit.html'
    model = Post
    fields = ['title','text']
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

class PostEditView(UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    fields = ['title','text']
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        form.instance.published_date = timezone.now()
        return super().form_valid(form)