from django.shortcuts import render

from recipes.models import Recipe

# Create your views here.


def profile_detail_view(request, user):
    obj_list = Recipe.objects.filter(user__username__icontains=user)
    context = {
        'profile_name': user,
        'obj_list': obj_list
    }
    return render(request, 'profiles/profile_detail.html', context)
