from django.contrib import admin
from .models import Story, Choice, ChoiceRecord

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    # actions_on_bottom = True
    readonly_fields = ["pub_date"]
    fields = ("title", "body", "pub_date")
    search_fields = ["title", "body"]

class ChoiceRecordAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Story, StoryAdmin)
admin.site.register(Choice)
admin.site.register(ChoiceRecord)