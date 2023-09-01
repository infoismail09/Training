from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Country,State,City

class CountryAdmin(ImportExportModelAdmin):
    list_display = ("short_name", "name", "country_code")
    search_fields = ("short_name", "name", "country_code")
    ordering = ("name",)


class StateAdmin(ImportExportModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)
    list_filter = ("country",)
    ordering = ("name",)


class CityAdmin(ImportExportModelAdmin):
    list_display = ("name", "state")
    search_fields = ("name",)
    list_filter = ("state", "state__country")
    ordering = ("name",)


# Now register the new UserAdmin...
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
