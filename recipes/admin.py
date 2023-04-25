from django.contrib import admin

from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']
    search_fields = ['user__username', 'title', 'description']


admin.site.register(Recipe, RecipeAdmin)
