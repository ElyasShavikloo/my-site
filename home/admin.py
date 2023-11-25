from django.contrib import admin

from blog.admin import FilterTitle
from . import models


@admin.register(models.Project)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "customer", "status", "show_image")
    list_filter = ("created", FilterTitle)
    search_fields = ("title", "body", "created", "category")


admin.site.register(models.Message)
admin.site.register(models.ProjectCategories)
