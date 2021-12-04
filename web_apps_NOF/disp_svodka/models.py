from django.db import models
from web_apps_NOF.models import BaseModelDispSvodkaAbstract


class DispSvodkaStoredProcedures(BaseModelDispSvodkaAbstract):
    class Meta:
        verbose_name = 'Хранимая процедура'
        verbose_name_plural = 'Хранимые процедуры'


class NameTabsOfDispSvodka(BaseModelDispSvodkaAbstract):
    production = models.ForeignKey('DispSvodkaStoredProcedures', on_delete=models.PROTECT, null=True,
                                   verbose_name='Хранимая процедура',
                                   related_name='DispSvodkaStoredProcedures')
    class Meta:
        verbose_name = 'Имя таблицы дисп. сводки'
        verbose_name_plural = 'Имена таблиц дисп. сводки'
