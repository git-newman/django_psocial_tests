from django.db import models
from src.profiles.models import UserNet
from config import settings
from src.comments.models import AbstractComment
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Post(models.Model):
    """модель поста"""

    text = models.TextField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'POST by {self.user}'

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return f'{self.user} - {self.post}'
