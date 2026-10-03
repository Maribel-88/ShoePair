from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
]

# ⚠️ CRUCIAL: This links the media folder to your web browser!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customizing the Admin panel headers
admin.site.site_header = "ShoePair Admin Dashboard"
admin.site.site_title = "ShoePair Admin Portal"
admin.site.index_title = "Welcome to the ShoePair Catalog Manager"
