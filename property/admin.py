from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    search_fields = ('town',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('likes',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat',)
    raw_id_fields = ('user', 'flat',)
