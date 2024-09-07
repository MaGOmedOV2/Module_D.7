from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    models = Post
    queryset = Post.objects.order_by('time_in')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class PostDetail(DetailView):
    models = Post
    template_name = 'news_id.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.all()

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_edit.html'

    def form_valid(self, form):
        artic = form.save(commit=False)
        artic.Category = 2
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ArticlesUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'articles_edit.html'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')

