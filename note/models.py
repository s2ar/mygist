from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name="Текст/Код")
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано"
    )


    class Meta:
        verbose_name_plural = 'Заметки'
        verbose_name = 'Заметка'
        ordering = ['-published']
