from django.contrib import admin
from .models  import Category, staff,Sponsors,Carousel



class FirstAdmin(admin.ModelAdmin):
    list_display=("name","task","is_active",)
    list_editable=["is_active"]
    list_filter=("is_active","categories")
    readonly_fields=("slug",)

admin.site.register(staff,FirstAdmin)
admin.site.register(Category)
admin.site.register(Sponsors)
admin.site.register(Carousel)




