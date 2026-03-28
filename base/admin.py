from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Category, Variation

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'icon', 'language')
    
    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'language', 'icon'),
            'description': 'Manage category details and emoji icons'
        }),
    )

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [VariationInline]