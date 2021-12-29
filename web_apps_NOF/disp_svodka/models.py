from django.db import models
from web_apps_NOF.models import BaseModelDispSvodkaAbstract
import pypyodbc
from services import connecting_to_db, get_values_from_db
from django.db.models import JSONField
import json


class ServerNames(models.Model):
    name = models.CharField(default=None, max_length=200, blank=True)
    ip = models.CharField(default=None, max_length=150)
    user = models.CharField(default=None, max_length=150)
    password = models.CharField(default=None, max_length=150)

    class Meta:
        verbose_name = 'Cервер БД'
        verbose_name_plural = 'Сервера БД'


class DbNames(models.Model):
    name = models.CharField(default=None, max_length=200, blank=True)
    server_name = models.ForeignKey('ServerNames', on_delete=models.PROTECT, null=True)


class DbTableNames(models.Model):
    name = models.CharField(default=None, max_length=200, blank=True)
    db_name = models.ForeignKey('DbNames', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Имя таблицы БД'
        verbose_name_plural = 'Имена таблиц БД'


class DbFieldNames(models.Model):
    name = JSONField(null=True, blank=True)
    db_table_name = models.ForeignKey('DbTableNames', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Имя поля в таблице БД'
        verbose_name_plural = 'Имена полей в таблице БД'


class TabNames(models.Model):
    name = models.CharField(default=None, max_length=200, blank=True)
    name_en = models.CharField(max_length=200, blank=True)
    description = models.CharField(default=None, max_length=2000)

    class Meta:
        verbose_name = 'Имя таблицы дисп. сводки'
        verbose_name_plural = 'Имена таблиц дисп. сводки'


class TableHeads(models.Model):
    table_num = models.IntegerField(default=0)
    column_serial_num = models.IntegerField(default=0)
    field_value = models.CharField(blank=True, max_length=200)

    rowspan = models.IntegerField(default=1)
    colspan = models.IntegerField(default=1)
    class_name = models.CharField(default=None, max_length=500)
    thead_serial_num = models.IntegerField(default=0)
    tab_name = models.ForeignKey('TabNames', on_delete=models.PROTECT, null=True)

    thead_field_type = models.ForeignKey('THeadFieldTypes', on_delete=models.PROTECT, null=True,
                                         blank=True)

    class Meta:
        verbose_name = 'Шапка таблицы'
        verbose_name_plural = 'Шапки таблиц'

    @staticmethod
    def get_theads(tab_name, date_selected):
        theads = {}
        column_start = 1
        for th in TableHeads.objects.filter(tab_name__name_en=tab_name).order_by('table_num', 'thead_serial_num',
                                                                                 'column_serial_num'):
            column_end = column_start + th.colspan - 1
            table_num = th.table_num
            thead_serial_num = th.thead_serial_num

            if table_num not in theads.keys():
                theads.update({table_num: {}})
            if thead_serial_num not in theads[table_num].keys():
                theads[table_num].update({thead_serial_num: []})
                column_start = 1
                column_end = column_start + th.colspan - 1

            theads[table_num][thead_serial_num].append(
                {'field_value': date_selected if th.field_value == 'date' else th.field_value,
                 'colspan': str(th.colspan),
                 'rowspan': str(th.rowspan),
                 'class_name': th.class_name, 'column_start': column_start,
                 'column_end': column_end, 'row_start': '',
                 'row_end': ''})

            column_start = column_end
            column_start += 1
        # print(theads)
        return theads

    @staticmethod
    def get_tbody(table_name):
        tbody = {}
        tbody_dict = {}
        hour_counter = 1
        f = {}
        for i, th in enumerate(TableHeads.objects.filter(tab_name__name_en=table_name).order_by('table_num',
                                                                                                'thead_serial_num')):
            table_num = th.table_num
            thead_field_type = str(th.thead_field_type)
            if thead_field_type != 'info':

                if thead_field_type == 'work_shift_hour':
                    thead_field_type = thead_field_type + '-' + str(hour_counter)
                    hour_counter += 1
                else:
                    thead_field_type = thead_field_type + '-' + str(i)
                if table_num not in tbody.keys():
                    tbody.update({table_num: {}})
                tbody[table_num].update({thead_field_type: ''})

        # print(tbody)
        return tbody


class TableSiders(models.Model):
    table_num = models.IntegerField(default=0)
    column_serial_num = models.IntegerField(default=0)
    field_value = models.CharField(blank=True, max_length=200)
    rowspan = models.IntegerField(default=1)
    colspan = models.IntegerField(default=1)
    class_name = models.CharField(default=None, max_length=500)
    tsider_serial_num = models.IntegerField(default=0)
    tab_name = models.ForeignKey('TabNames', on_delete=models.PROTECT, null=True)
    db_field_name = models.ForeignKey('DbFieldNames', on_delete=models.PROTECT, null=True, blank=True)
    fields_type_and_request_index_dict = JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Боковик таблицы'
        verbose_name_plural = 'Боковики таблиц'

    @staticmethod
    def get_tsiders(tab_name, date_selected):
        column_start = 1
        tsiders = {}
        tbody = TableHeads.get_tbody(table_name=tab_name)
        for ts in TableSiders.objects.filter(tab_name__name_en=tab_name).order_by('table_num',
                                                                                  'tsider_serial_num',
                                                                                  'column_serial_num'):
            # print(ts.db_field_name)
            column_end = column_start + ts.colspan - 1
            tsider_serial_num = ts.tsider_serial_num
            table_num = ts.table_num
            if table_num not in tsiders.keys():
                tsiders.update({table_num: {}})
            if tsider_serial_num not in tsiders[table_num].keys():
                tsiders[table_num].update({tsider_serial_num: []})
                column_start = ts.column_serial_num + 1
                column_end = column_start + ts.colspan - 1

            tsiders[table_num][tsider_serial_num].append(
                {'field_value': date_selected if ts.field_value == 'date' else ts.field_value,
                 'colspan': str(ts.colspan),
                 'rowspan': str(ts.rowspan), 'class_name': str(ts.class_name),
                 'db_field_name': str(ts.db_field_name), 'column_start': column_start,
                 'column_end': column_end})
            # print(column_end, column_start)

            column_start = column_end
            # print(tsiders)
            if ts.db_field_name is not None:

                fields_type_and_request_index_dict = ts.fields_type_and_request_index_dict
                db_field_name = ', '.join(ts.db_field_name.name)

                # print(DbTableNames.objects.all())
                db_table_name = str(DbTableNames.objects.get(dbfieldnames__name=ts.db_field_name.name).name)

                database = str(DbNames.objects.get(dbtablenames__dbfieldnames__name=ts.db_field_name.name).name)

                server_name = str(
                    ServerNames.objects.get(dbnames__dbtablenames__dbfieldnames__name=ts.db_field_name.name).name)
                ip = str(ServerNames.objects.filter(name=server_name)[0].ip)

                user = str(ServerNames.objects.filter(name=server_name)[0].user)
                password = str(ServerNames.objects.filter(name=server_name)[0].password)

                # print(tbody)
                # print(ip, password, user, database, db_table_name, db_field_name, )
                tbody_values = get_values_from_db.get_values_from_db(server=ip, password=password, user=user,
                                                                     database=database,
                                                                     db_table_name=db_table_name,
                                                                     db_field_name=db_field_name,
                                                                     date_selected=date_selected,
                                                                     column_start=column_start,
                                                                     tbody=tbody[ts.table_num],
                                                                     fields_type_and_request_index_dict=fields_type_and_request_index_dict)
                # print(tbody_values)
                for el in tbody_values:
                    tsiders[table_num][tsider_serial_num].append(el)
            # print(tsiders)

            column_start += 1

    # print(tsiders)
        return tsiders


class RequestsToDB(models.Model):
    request_to_db = JSONField()

    # def __str__(self):
    #     return self.request_to_db


class THeadFieldTypes(models.Model):
    thead_field_name = models.CharField(max_length=200)
    request_to_db = models.ForeignKey('RequestsToDB', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.thead_field_name
