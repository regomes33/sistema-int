from django.contrib import admin

from .models import City, District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'admin':
            return True
        return False


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uf')
    search_fields = ('name',)
    list_filter = ('uf',)

    def has_delete_permission(self, request, obj=None):
        return False
