from django.contrib import admin

from kanban.models import Kanban
# Register your models here.

class AdminKanban(admin.ModelAdmin):
    list_display=('estado','created',)
    search_fields=('estado',)
    list_filter = ('created',)
    date_hierarchy = "created"
    

admin.site.register(Kanban,AdminKanban)