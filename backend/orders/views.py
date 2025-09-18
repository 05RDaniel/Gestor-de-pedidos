from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count, Q
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def reporting(request):
    avg_delivery_time = Shipment.objects.filter(delivered_at__isnull=False).aggregate(
        avg_time=Avg(models.F('delivered_at') - models.F('shipped_at'))
    )['avg_time']
    
    pending_orders = Order.objects.filter(delivered_at__isnull=True).count()
    volume_by_customer = Order.objects.values('customer').annotate(total=Count('id'))

    return Response({
        "avg_delivery_time": avg_delivery_time,
        "pending_orders": pending_orders,
        "volume_by_customer": list(volume_by_customer)
    })
