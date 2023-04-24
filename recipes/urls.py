from django.urls import path

from .views import recipes_detail_view, recipes_list_view

urlpatterns = [
    path('', recipes_list_view, name='recipes-list'),
    path('<int:id>/', recipes_detail_view, name='recipes-detail')
]
