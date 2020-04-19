from django.contrib import admin
from .models import *

class ReportAdmin(admin.ModelAdmin):
    list_display=('Name','TL')
    list_display_links=['Name']
    search_fields=['Name']
    list_per_page=25


admin.site.register(Report,ReportAdmin)
