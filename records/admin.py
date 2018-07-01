from django.contrib import admin
from .models import Category, SittingDate, ParliamentRecord

# Register your models here.
admin.site.register(Category)
admin.site.register(SittingDate)

@admin.register(ParliamentRecord)
class ParliamentRecordAdmin(admin.ModelAdmin):
    list_display = ('title','sitting_date', 'display_category')
