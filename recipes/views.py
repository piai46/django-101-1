from django.shortcuts import get_object_or_404, render

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
