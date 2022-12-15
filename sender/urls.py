from django.urls import path, include
from sender.routers import *


urlpatterns = [
    path('api/', include(router_client.urls)),
    path('api/', include(router_queue.urls)),


]