from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'prod_date', 'creation_time', 'update_time']
    search_fields = ['name']
    list_filter = ['prod_date']
    fieldsets = (
        ('Name', {'fields': ['name']}),
        ('Production Year', {'fields': ['prod_date']})
    )

