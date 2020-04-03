from django.contrib import admin

from .models import *

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(BaseItem , ItemsAdmin)
admin.site.register(Refrigerator , ItemsAdmin)
admin.site.register(Television , ItemsAdmin)
admin.site.register(Laptob , ItemsAdmin)
admin.site.register(Mobile , ItemsAdmin)
admin.site.register(Book , ItemsAdmin)
admin.site.register(Stationery , ItemsAdmin)
admin.site.register(TopProduct)
admin.site.register(AmazingOffer)