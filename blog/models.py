from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url_detail(self):
        return reverse("article-detail", kwargs={"id": self.id})

    def get_absolute_url_edit(self):
        return reverse("article-edit", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("article-delete", kwargs={"id": self.id})
