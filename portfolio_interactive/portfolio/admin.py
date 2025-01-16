from django.contrib import admin
from .models import Project, ContactFormSubmission

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)


@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')  # Поля, отображаемые в списке
    list_filter = ('submitted_at',)  # Фильтр по дате
    search_fields = ('name', 'email', 'message')  # Поля для поиска
    ordering = ('-submitted_at',)  # Сортировка по убыванию даты