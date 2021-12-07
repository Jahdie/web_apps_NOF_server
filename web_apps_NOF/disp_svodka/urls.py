from django.urls import path
from .views import *


app_name = 'disp_svodka'


urlpatterns = [
    path('', disp_svodka_controller, name='disp_svodka'),
    path('<str:current_date>/<str:table_name>/', get_table_of_dispatchers_summary_by_tab_name, name='table_name'),
]