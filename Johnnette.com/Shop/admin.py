from django.contrib import admin
from .models import (
    Address,
    Product,
    Cart,
    OrderPlaced
)


@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'locality', 'city', 'pincode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'brand_name', 'product_title', 'selling_price', 'actual_price']
    

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'product', 'quantity', 'total_cost']
    


from django.utils.html import format_html
from django.urls import reverse
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'customer_info', 'product_info', 'quantity', 'total_amount', 'payment_status', 'status']
    
    def customer_info(self, obj):
        link = reverse("admin:Shop_address_change", args=[obj.address.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.address.full_name)

        
    def product_info(self, obj):
        link = reverse("admin:Shop_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.brand_name)