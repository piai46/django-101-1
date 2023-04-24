from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe

# Create your views here.


def recipes_list_view(request):
    obj = Recipe.objects.all()
    context = {'objects': obj}
    return render(request, 'recipes/list.html', context)


def recipes_detail_view(request, id):
    obj = get_object_or_404(Recipe, id=id)
    context = {'obj': obj}
    return render(request, 'recipes/detail.html', context)


@login_required
def recipes_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect(obj)  # arrumar isso
    context = {'form': form}
    return render(request, 'recipes/recipes_create.html', context)
