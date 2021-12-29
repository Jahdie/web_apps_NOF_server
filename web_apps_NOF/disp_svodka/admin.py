from django.contrib import admin
from .models import *


class TableHeadsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'table_num', 'field_value', 'colspan', 'rowspan', 'class_name', 'thead_serial_num',
        'column_serial_num',
        'tab_name', 'thead_field_type', )
    list_filter = ('id', 'field_value')


class TableSidersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'table_num', 'field_value', 'colspan', 'rowspan', 'class_name', 'tsider_serial_num', 'column_serial_num',
        'tab_name', 'db_field_name', 'fields_type_and_request_index_dict')
    list_filter = ('id', 'field_value',)


MODELS_LIST = [TabNames, ServerNames, DbTableNames, DbFieldNames, DbNames, RequestsToDB, THeadFieldTypes]

admin.site.register(MODELS_LIST)
admin.site.register(TableHeads, TableHeadsAdmin)
admin.site.register(TableSiders, TableSidersAdmin)
