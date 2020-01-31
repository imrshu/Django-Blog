from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField()
    is_private = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name
