from django.contrib import admin
from ALL import models

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','title', 'date_of_creation', 'completed']
    readonly_fields = ("date_of_creation", )

admin.site.register(models.Task,TaskAdmin)