from django.urls import path

from .views import (recipes_create_view, recipes_delete_view,
                    recipes_detail_view, recipes_edit_view, recipes_list_view,
                    recipes_search_view)

urlpatterns = [
    path('', recipes_list_view, name='recipes-list'),
    path('search/', recipes_search_view, name='recipes-search'),
    path('create/', recipes_create_view, name='recipes-create'),
    path('<slug:slug>/', recipes_detail_view, name='recipes-detail'),
    path('<slug:slug>/edit/', recipes_edit_view, name='recipes-edit'),
    path('<slug:slug>/delete/', recipes_delete_view, name='recipes-delete'),
]
