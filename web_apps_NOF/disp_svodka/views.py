from django.shortcuts import render
from django.template.loader import render_to_string
from .models import *
from django.http import JsonResponse, HttpResponse
import openpyxl


def index(request):
    context = {}
    return render(request, 'base.html')


def disp_svodka_controller(request):
    context = {'tabs': NameTabsOfDispSvodka.objects.all()}
    # for item in context['tabs']:
    #     print(item.)
    return render(request, 'disp_svodka/base.html', context)


def get_table_of_dispatchers_summary_by_tab_name(request, current_date, table_name):
    if request.is_ajax():
        # TableHead.objects.all().update(rowspan=1)
        # i = 0
        # for th in table_thead_2:
        #     i += 1
        #     print(th['name_field'])
        #     TableHead.objects.create(field_name=th['name_field'], colspan=th['colspan'], column_serial_num=i,
        #                              class_name='table-light', table_thead_serial_num=2, name_tabs_of_disp_svodka_id=1, scope='col')
        context = {'table_thead': TableHead.get_table_heads(table_name=table_name, current_date=current_date)}
        return render(request, 'disp_svodka/test.html', context)
