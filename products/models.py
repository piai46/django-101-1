from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=True, null=True)
    featured = models.BooleanField()

    def get_absolute_url_detail(self):
        return reverse("product-detail", kwargs={"id": self.id})

    def get_absolute_url_edit(self):
        return reverse("product-edit", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("product-delete", kwargs={"id": self.id})
