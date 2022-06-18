from django.contrib import admin
from .models import Actor


admin.site.site_header = 'Admin Panel'

admin.site.site_title = 'Admin Panel'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'profile_pic', 'my_custom_function_field']
    search_fields = ['name']
    list_filter = ['gender']
    fieldsets = (
        ('Name', {'fields': ['name']}),
        ('Gender', {'fields': ['gender']})
    )

    def my_custom_function_field(self, obj):
        actor_age = obj.age

        return f"{actor_age}"

    my_custom_function_field.short_description = 'Actor Age'

