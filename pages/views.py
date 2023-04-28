from django.db.models import Q
from django.shortcuts import render

from blog.models import Article
from products.models import Product
from recipes.models import Recipe

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def search_view(request):
    query = request.GET['query']
    recipe_query_set = Recipe.objects.all()  # Para caso <query> for None, ele retorna Todos os resultados
    article_query_set = Article.objects.all()  # Para caso <query> for None, ele retorna Todos os resultados
    product_query_set = Product.objects.all()  # Para caso <query> for None, ele retorna Todos os resultados
    if query:
        recipe_query_set = Recipe.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(user__username__icontains=query)
        )
        article_query_set = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        product_query_set = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    context = {
        'recipe_list': recipe_query_set,
        'article_list': article_query_set,
        'product_list': product_query_set,
    }
    return render(request, 'search_result.html', context)
