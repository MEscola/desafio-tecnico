from django.contrib import admin
from .models import Projects, SubItem

class SubItemInline(admin.TabularInline):
    model = SubItem
    extra = 0  # Não exibe linhas vazias extras

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [SubItemInline]