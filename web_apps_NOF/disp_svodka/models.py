from django.db import models
from web_apps_NOF.models import BaseModelDispSvodkaAbstract


class DispSvodkaStoredProcedures(BaseModelDispSvodkaAbstract):
    class Meta:
        verbose_name = 'Хранимая процедура'
        verbose_name_plural = 'Хранимые процедуры'


class NameTabsOfDispSvodka(BaseModelDispSvodkaAbstract):
    stored_procedures = models.ForeignKey('DispSvodkaStoredProcedures', on_delete=models.PROTECT, null=True,
                                          verbose_name='Хранимая процедура',
                                          related_name='DispSvodkaStoredProcedures')

    class Meta:
        verbose_name = 'Имя таблицы дисп. сводки'
        verbose_name_plural = 'Имена таблиц дисп. сводки'


class TableHead(models.Model):
    column_serial_num = models.IntegerField(default=0)
    field_name = models.CharField(default=None, max_length=20)
    scope = models.CharField(default=None, max_length=20)
    rowspan = models.IntegerField(default=1)
    colspan = models.IntegerField(default=0)
    class_name = models.CharField(default=None, max_length=50)
    table_thead_serial_num = models.IntegerField(default=0)
    name_tabs_of_disp_svodka = models.ForeignKey('NameTabsOfDispSvodka', on_delete=models.PROTECT, null=True)


    @staticmethod
    def get_table_heads(table_name, current_date):
        th_dict = {}
        for th in TableHead.objects.filter(name_tabs_of_disp_svodka__stored_procedures__name=table_name).order_by('table_thead_serial_num'):
            table_thead_serial_num = th.table_thead_serial_num
            if table_thead_serial_num not in th_dict.keys():
                th_dict.update({table_thead_serial_num: []})
            th_dict[table_thead_serial_num].append(
                {'field_name': current_date if th.field_name == 'date' else th.field_name, 'colspan': str(th.colspan),
                 'rowspan': str(th.rowspan),
                 'class_name': th.class_name})
        print(th_dict)
        return th_dict
