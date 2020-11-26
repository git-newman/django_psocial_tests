from django.db import models


class AbstractComment(models.Model):
    text = models.TextField("Сообщение", max_length=512)
    created_date = models.DateTimeField("Дата добавления", auto_now_add=True)
    update_date = models.DateTimeField("Дата добавления", auto_now=True)
    published = models.BooleanField("Опубликовать", default=True)
    deleted = models.BooleanField("Удален?", default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract = True


