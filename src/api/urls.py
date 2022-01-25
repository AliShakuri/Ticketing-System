from django.urls import path, include
from .views import TicketViewSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('tickets', TicketViewSet, basename="tickets")

urlpatterns = [
    path("", include(router.urls)),
]
