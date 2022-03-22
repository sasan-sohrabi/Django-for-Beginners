from django.db import models


class Posts(models.Model):
    post = models.TextField()

    def __str__(self):
        return self.post[:50]
