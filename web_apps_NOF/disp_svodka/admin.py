from django.contrib import admin
from .models import *


class TableHeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_name', 'scope', 'colspan', 'rowspan', 'class_name', 'table_thead_serial_num', 'column_serial_num',
                    'name_tabs_of_disp_svodka')
    list_filter = ('id', 'field_name')


MODELS_LIST = [DispSvodkaStoredProcedures, NameTabsOfDispSvodka]

admin.site.register(MODELS_LIST)
admin.site.register(TableHead, TableHeadAdmin)
