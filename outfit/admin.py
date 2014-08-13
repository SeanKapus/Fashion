from django.contrib import admin
from outfit.models import Clothes, User


class ClothesAdmin(admin.ModelAdmin):
    # 'TYPE_CHOICES' won't work here, need to use 'type' or 'get_type_display'
    list_display = ('name', 'TYPE_CHOICES',)


admin.site.register(Clothes)
admin.site.register(User)
