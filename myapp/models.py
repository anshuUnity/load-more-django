from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
