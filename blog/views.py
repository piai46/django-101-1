from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import ArticleModelForm
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()  # <appname>/<modelname>_<view type>.html


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        # id_ = self.kwargs.get('id')
        # return get_object_or_404(Article, id=id_)
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug_)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'  # <appname>/<modelname>_<view type>.html
    form_class = ArticleModelForm
    success_url = '/blog/'


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    success_url = '/blog/'

    def get_object(self):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug_)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    success_url = '/blog/'

    def get_object(self):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug_)
