"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (product_create_view, product_delete_view,
                    product_detail_view, product_edit_view, product_list_view,
                    product_search_view)

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/edit/', product_edit_view, name='product-edit'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('search/', product_search_view, name='product-search'),
]
