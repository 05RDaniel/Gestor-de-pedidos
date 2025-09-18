from django.db import models
from django.utils import timezone

class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=20, editable=False)
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Solo generar el id en la primera creación
        if not self.id:
            today = timezone.now().date()
            date_str = today.strftime("%Y%m%d")  # AAAAMMDD

            # Contar cuántos pedidos existen hoy
            count_today = Order.objects.filter(
                id__startswith=date_str
            ).count() + 1

            # Formatear con 3 dígitos
            seq = str(count_today).zfill(3)

            # Generar ID final
            self.id = f"{date_str}{seq}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.customer} ({self.product})"
