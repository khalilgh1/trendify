from django.contrib import admin
from .models import Product, Category, Variation
# Register your models here.
admin.site.register(Category)

class VariationInline(admin.TabularInline):  # or admin.StackedInline for vertical layout
    model = Variation
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationInline]
