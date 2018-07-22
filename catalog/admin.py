from django.contrib import admin
from .models import Story
from .models import Product

#admin.site.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'Author', 'id', 'Date_added', 'featured')

class ProductAdmin(admin.ModelAdmin):
    list_dispaly = ('name', 'price', 'id', 'Date_added' )

admin.site.register(Story, StoryAdmin)
admin.site.register(Product, ProductAdmin)
