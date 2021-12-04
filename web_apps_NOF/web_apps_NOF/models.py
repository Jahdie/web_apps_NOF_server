from django.db import models

class BaseModelDispSvodkaAbstract(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


    def __str__(self):
        return self.name


    class Meta:
        abstract = True
