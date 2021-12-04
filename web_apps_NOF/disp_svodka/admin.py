from django.contrib import admin
from .models import *

MODELS_LIST = [DispSvodkaStoredProcedures, NameTabsOfDispSvodka]

admin.site.register(MODELS_LIST)