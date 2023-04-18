from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url_detail(self):
        return reverse("article-detail", kwargs={"slug": self.slug})

    def get_absolute_url_edit(self):
        return reverse("article-edit", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("article-delete", kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + f'-{self.id}'
            self.save()
