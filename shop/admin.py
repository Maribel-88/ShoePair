# Inside shop/admin.py
from django.contrib import admin
from .models import Product

# Customizing how Products display and edit inside the Admin Dashboard
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Displays clean columns inside your product list layout
    list_display = ('name', 'price', 'stock', 'is_active', 'has_image')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    
    # Custom helper function showing a checkbox indicator if an image exists
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image Uploaded'
