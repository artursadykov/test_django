from django.contrib import admin
from .models import *

class NoteAdmin (admin.ModelAdmin):
    #list_display = ["contents"]
    #exclude = ["contents"]
    list_display = [field.name for field in Note._meta.fields]
    list_filter = ["contents"]
    search_fields = ["contents"]

    class Meta:
        model: Note

admin.site.register(Note,NoteAdmin)

class NoteTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NoteType._meta.fields]

    class Meta:
        model: NoteType

admin.site.register(NoteType,NoteTypeAdmin)

