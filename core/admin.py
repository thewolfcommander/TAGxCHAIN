from core.models import Country, Exchange, Scripts
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
class CountryAdmin(ImportExportActionModelAdmin):
    pass

class ExchangeAdmin(ImportExportActionModelAdmin):
    pass

class ScriptsAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Scripts, ScriptsAdmin)