from django.contrib import admin
from .models import Task, SubTask, Category


def mark_tasks_done(modeladmin, request, queryset):
    queryset.update(status='Done')


mark_tasks_done.short_description = "Mark selected tasks as Done"


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'created_at', 'deadline')
    search_fields = ('title', 'description')
    ordering = ('-deadline',)
    actions = [mark_tasks_done]
    inlines = [SubTaskInline]


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at', 'task')
    list_filter = ('status', 'created_at', 'deadline')
    search_fields = ('title', 'description')
    ordering = ('status', 'deadline')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
