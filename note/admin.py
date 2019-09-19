from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'published')


admin.site.register(Note, NoteAdmin)
