from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'archived')
    list_filter = ('archived',)
    search_fields = ('title','content')
