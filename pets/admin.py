from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    exclude = ("elo_rating",)
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Pet, PetAdmin)
