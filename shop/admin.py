# Inside shop/admin.py
from django.contrib import admin
from .models import Product, Size

# Register the raw sizes list so you can manage the master UK size run list
admin.site.register(Size)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Added 'get_sizes' display column to the admin table view
    list_display = ('name', 'price', 'stock', 'get_sizes', 'is_active', 'has_image')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    
    # NEW: Displays sizes cleanly inside the item editing form as a filter grid box
    filter_horizontal = ('sizes',)
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image Uploaded'

    # NEW: Helper function to display sizes in a comma-separated format on the list page
    def get_sizes(self, obj):
        return ", ".join([p.name for p in obj.sizes.all()])
    get_sizes.short_description = 'Available UK Sizes'
