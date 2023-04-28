from django.urls import path

from .views import (recipes_create_view, recipes_delete_view,
                    recipes_detail_view, recipes_edit_view, recipes_list_view)

app_name = 'recipes'
urlpatterns = [
    path('', recipes_list_view, name='list'),
    path('create/', recipes_create_view, name='create'),
    path('<slug:slug>/', recipes_detail_view, name='detail'),
    path('<slug:slug>/edit/', recipes_edit_view, name='edit'),
    path('<slug:slug>/delete/', recipes_delete_view, name='delete'),
]
