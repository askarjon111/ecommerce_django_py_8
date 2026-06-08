from django.db import models
from django.db.models import Sum, F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.users.models import User
from apps.common.models import BaseModel
from apps.products.models import Product

# Create your models here.

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Buyurtma #{self.id} | Mijoz: {self.user.username} | Manzil: {self.address}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Buyurtma #{self.order.id})"

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)


@receiver([post_save, post_delete], sender=OrderItem)
def update_order_total_price(sender, instance, **kwargs):
    """
    Order ichidagi biror mahsulot miqdori o'zgarganda, qo'shilganda yoki o'chirilganda
    Order-ning umumiy narxini (total_price) qayta hisoblaydi.
    """
    order = instance.order
    
    # Barcha OrderItem-larning (narxi * miqdori) yig'indisini bazadan hisoblab olamiz
    total = order.items.aggregate(
        total=Sum(F('price') * F('quantity'))
    )['total'] or 0.00
    
    # Order-ning umumiy narxini yangilaymiz
    order.total_price = total
    order.save(update_fields=['total_price'])