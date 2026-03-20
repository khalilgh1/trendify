from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Category, Variation

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [VariationInline]