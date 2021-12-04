from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

def index(request):
    context = {}
    return render(request, 'base.html')

def disp_svodka_controller(request):
    context = {'is_visible': 'hidden'}
    context = {'btn': ['1','2','3','4','5']}
    return render(request, 'disp_svodka/base.html', context)

def table_name(request, current_date, table_name):

    if request.is_ajax():
        print(current_date, table_name)
        context = {'test': 'test!!!'}
        result = render_to_string('disp_svodka/test.html', context)
        print(result)
        # return JsonResponse({'result': result})
        # return HttpResponse("11111")
        return render(request, 'disp_svodka/test.html', context)

