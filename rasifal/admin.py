from django.contrib import admin
from .models import Rasifal, Rasifal_Desc
# Register your models here.
admin.site.register(Rasifal)


class RasifalDescAdmin(admin.ModelAdmin):
    list_display = ('rasi', 'date')
    readonly_fields = ('date', )


admin.site.register(Rasifal_Desc, RasifalDescAdmin)