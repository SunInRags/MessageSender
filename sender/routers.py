from rest_framework import routers
from sender import views

router_queue = routers.SimpleRouter()
router_queue.register(r'queue', views.QueueViewSet)
router_client = routers.SimpleRouter()
router_client.register(r'client', views.ClientViewSet)