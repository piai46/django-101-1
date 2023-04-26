from django.urls import path

from .views import profile_detail_view

urlpatterns = [
    path('<slug:user>/', profile_detail_view, name='profile-detail'),
]
