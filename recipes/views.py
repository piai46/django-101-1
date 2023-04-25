from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe

# Create your views here.


def recipes_list_view(request):
    obj = Recipe.objects.all()
    context = {'objects': obj}
    return render(request, 'recipes/recipe_list.html', context)


def recipes_detail_view(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    context = {'obj': obj}
    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def recipes_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect(obj)
    context = {'form': form}
    return render(request, 'recipes/recipe_create.html', context)


@login_required
def recipes_edit_view(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    form = RecipeForm(request.POST or None, instance=obj)
    if form.is_valid():
        saved_obj = form.save()
        return redirect(saved_obj)
    context = {
        'form': form
    }
    return render(request, 'recipes/recipe_edit.html', context)


@login_required
def recipes_delete_view(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'recipes/recipe_delete.html', context)


def recipes_search_view(request):
    query = request.GET['query']
    query_set = Recipe.objects.all()  # Para caso <query> for None, ele retorna Todos os resultados
    if query:
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        query_set = Recipe.objects.filter(lookups)
    context = {
        'obj_list': query_set
    }
    return render(request, 'recipes/recipe_search.html', context)
