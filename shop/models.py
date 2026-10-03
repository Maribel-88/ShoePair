# Inside shop/models.py
from django.db import models

class Size(models.Model):
    # UK Sizes can include half sizes (e.g., 6.5, 9.5), so we use a CharField
    name = models.CharField(max_length=10, unique=True, help_text="e.g., UK 6, UK 8.5")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shoes/', blank=True, null=True)
    
    # NEW: Link products to multiple UK sizes
    sizes = models.ManyToManyField(Size, blank=True, help_text="Select all available UK sizes for this shoe")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
