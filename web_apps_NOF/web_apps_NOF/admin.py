from django.contrib import admin
from disp_svodka.models import *

MODELS_LIST = [DispSvodkaStoredProcedures, NameTabsOfDispSvodka]

admin.site.register(MODELS_LIST)