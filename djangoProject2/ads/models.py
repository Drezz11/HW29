
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


    class Mera:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    # address = models.CharField(max_length=300)
    # locations = models.ManyToManyField("Location")
    is_published = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="pictures")

    class Mera:
        verbose_name = "Объявления"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name