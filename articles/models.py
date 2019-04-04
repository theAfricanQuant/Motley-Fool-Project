from django.db import models


class Comment(models.Model):
    comment = models.CharField(max_length=500, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    article_uuid = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.comment[:50]