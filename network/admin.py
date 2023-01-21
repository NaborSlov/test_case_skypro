from django.contrib import admin, messages
from django.utils.translation import ngettext

from network import models


@admin.register(models.Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "product",)
    list_display_links = ("title",)
    search_fields = ("contact__city",)


@admin.register(models.RetailsNet)
@admin.register(models.IndiPred)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "product", "indebtedness")
    list_display_links = ("title",)
    search_fields = ("contact__city",)
    actions = ("debt_deletion",)

    @admin.action(description="Удаление задолжности")
    def debt_deletion(self, request, queryset):
        updates = queryset.update(indebtedness=0.00)
        self.message_user(request, ngettext("%d задолжность удалена",
                                            "%d задолности удалены", updates) % updates, messages.SUCCESS)


admin.site.register(models.Product)
admin.site.register(models.Contact)
