from django.contrib import admin
from .models import *


class showTable(admin.ModelAdmin):
    list_display = ('image_tag','title','created_at')
    ordering = ('title',)
    search_fields = ('title',)
    list_per_page = 3
class showTable_profile(admin.ModelAdmin):
    list_display = ('image_tag','user_name','join')
    ordering = ('user_name',)
    search_fields = ('user_name',)
    # list_per_page = 3

# Register your models here.
admin.site.register(BlogModel,showTable)
admin.site.register(profile,showTable_profile)
