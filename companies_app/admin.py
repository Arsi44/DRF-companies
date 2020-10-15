from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Category, Company, Product


class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'title_cat',)
    list_display_links = ('id', 'title_cat',)


admin.site.register(Category, CategoryAdmin)


class CompanyAdmin(admin.ModelAdmin):
    """Компании"""
    list_display = ('id', 'title_com', 'description_com', 'company_is_active',)
    list_display_links = ('id', 'title_com',)


admin.site.register(Company, CompanyAdmin)


class ProductAdmin(admin.ModelAdmin):
    """Продукты"""
    list_display = ('id', 'title', 'company', 'description_prod', 'is_active',)
    list_display_links = ('id', 'title',)


admin.site.register(Product, ProductAdmin)