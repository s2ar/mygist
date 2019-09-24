from django.contrib import admin
from .models import Note
from .models import Category


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'published')


admin.site.register(Note, NoteAdmin)
admin.site.register(Category)
