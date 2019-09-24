from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(verbose_name="Текст/Код")
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано"
    )
    category = models.ForeignKey(
        'Category', null=True,
        on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Заметки'
        verbose_name = 'Заметка'
        ordering = ['-published']


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


