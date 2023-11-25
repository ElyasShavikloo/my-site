from django.contrib import admin
from . import models


class FilterTitle(admin.SimpleListFilter):
    title = "عناوین پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('inter', 'اینتر'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInLine(admin.TabularInline):
    model = models.CommentModel


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "show_image")
    list_filter = ("created", FilterTitle)
    search_fields = ("title", "body", "created", "category")
    inlines = (CommentInLine,)


admin.site.register(models.Category)
admin.site.register(models.CommentModel)
admin.site.register(models.Like)

