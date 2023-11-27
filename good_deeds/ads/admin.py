from django.contrib import admin
from .models import Category, Ad, AdRequest, ApplicantList


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'pub_date']
    list_filter = ['category', 'pub_date']
    search_fields = ['title', 'description']


@admin.register(AdRequest)
class AdRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'ad', 'pub_date', 'comment']
    list_filter = ['pub_date']
    search_fields = ['user__username', 'ad__title']


@admin.register(ApplicantList)
class ApplicantListAdmin(admin.ModelAdmin):
    list_display = ['ad', 'user', 'is_selected']
    list_filter = ['ad', 'is_selected']
    search_fields = ['user__username', 'ad__title']
