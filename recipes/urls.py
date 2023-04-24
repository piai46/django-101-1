from django.urls import path

from .views import recipes_create_view, recipes_detail_view, recipes_list_view

urlpatterns = [
    path('', recipes_list_view, name='recipes-list'),
    path('<int:id>/', recipes_detail_view, name='recipes-detail'),
    path('create/', recipes_create_view, name='recipes-create'),
]
