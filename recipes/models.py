from django.db import models
from django.urls import reverse

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"id": self.id})

    def get_absolute_url_edit(self):
        return reverse("recipes-edit", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("recipes-delete", kwargs={"id": self.id})
