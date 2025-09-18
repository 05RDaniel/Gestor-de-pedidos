from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import OrderViewSet, reporting

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/reporting/', reporting),
]
