from django.db import models
from django.utils import timezone
from django.db.models.functions import Now

class Posts(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    # -------------------------------------------------------
    title = models.CharField(max_length=300,)
    slug = models.SlugField(max_length=300, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # saved_on_db_time = models.DateTimeField(db_default=Now())
    status = models.CharField(max_length=2,
                              choices=Status,
                              default=Status.DRAFT,
                              )


    class Meta:
        ordering=["-publish"]
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.title
    