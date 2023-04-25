from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

User = settings.AUTH_USER_MODEL


class Recipe(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"slug": self.slug})

    def get_absolute_url_edit(self):
        return reverse("recipes-edit", kwargs={"slug": self.slug})

    def get_absolute_url_delete(self):
        return reverse("recipes-delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + f'-{self.id}'
            self.save()
