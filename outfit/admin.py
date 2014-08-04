from django.contrib import admin
from outfit.models import Clothes, User


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'TYPE_CHOICES',)


admin.site.register(Clothes)
admin.site.register(User)
