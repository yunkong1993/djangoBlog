from django.contrib import admin
from .models import VisitNumber, Userip


class ReadOnlyModelAdmin(admin.ModelAdmin):
    """ModelAdmin class that prevents modifications through the admin.

    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    """

    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(ReadOnlyModelAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False


class VisitNumberAdmin(ReadOnlyModelAdmin):
    list_display = ['day', 'day_count', 'count']


class UseripAdmin(ReadOnlyModelAdmin):
    list_display = ['ip', 'count']


admin.site.register(VisitNumber, VisitNumberAdmin)
admin.site.register(Userip, UseripAdmin)